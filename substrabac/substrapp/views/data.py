import ntpath
import os
import re

from django.db import IntegrityError
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from substrapp.models import Data, Dataset
from substrapp.serializers import DataSerializer, LedgerDataSerializer
from substrapp.utils import get_hash


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


class DataViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  # mixins.UpdateModelMixin,
                  # mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        data = request.data

        # check if bulk create
        files = request.data.getlist('files', None)
        dataset_keys = data.getlist('dataset_keys')
        dataset_count = Dataset.objects.filter(pkhash__in=dataset_keys).count()

        # check all dataset exists
        if dataset_count != len(dataset_keys):
            return Response({
                'message': f'One or more dataset keys provided do not exist in local substrabac database. Please create them before. Dataset keys: {dataset_keys}'},
                status=status.HTTP_400_BAD_REQUEST)
        else:

            # bulk
            if files:

                l = []
                for x in files:
                    file = request.FILES[path_leaf(x)]
                    l.append({
                        'pkhash': get_hash(file),
                        'file': file
                    })

                serializer = self.get_serializer(data=l, many=True)
                try:
                    serializer.is_valid(raise_exception=True)
                except Exception as e:
                    return Response({
                        'message': e.args,
                        'pkhash': [x['pkhash'] for x in l]},
                        status=status.HTTP_409_CONFLICT)
                else:
                    # create on db
                    try:
                        instances = self.perform_create(serializer)
                    except Exception as exc:
                        return Response({'message': exc.args},
                                        status=status.HTTP_400_BAD_REQUEST)
                    else:
                        # init ledger serializer
                        ledger_serializer = LedgerDataSerializer(data={'test_only': data.get('test_only', False),
                                                                       'dataset_keys': dataset_keys,
                                                                       'instances': instances},
                                                                 context={'request': request})

                        if not ledger_serializer.is_valid():
                            # delete instance
                            for instance in instances:
                                instance.delete()
                            raise ValidationError(ledger_serializer.errors)

                        # create on ledger
                        data, st = ledger_serializer.create(ledger_serializer.validated_data)

                        if st not in [status.HTTP_201_CREATED, status.HTTP_202_ACCEPTED]:
                            return Response(data, status=st)

                        headers = self.get_success_headers(serializer.data)
                        for d in serializer.data:
                            if d['pkhash'] in data['pkhash'] and data['validated'] is not None:
                                d['validated'] = data['validated']
                        return Response(serializer.data, status=st, headers=headers)
            else:
                file = data.get('file')
                pkhash = get_hash(file)
                d = {
                    'pkhash': pkhash,
                    'file': file
                }
                serializer = self.get_serializer(data=d)

                try:
                    serializer.is_valid(raise_exception=True)
                except Exception as e:
                    return Response({
                        'message': e.args,
                        'pkhash': pkhash},
                        status=status.HTTP_400_BAD_REQUEST)
                else:
                    # create on db
                    try:
                        instance = self.perform_create(serializer)
                    except Exception as exc:
                        return Response({'message': exc.args},
                                        status=status.HTTP_400_BAD_REQUEST)
                    else:
                        # init ledger serializer
                        ledger_serializer = LedgerDataSerializer(data={'test_only': data.get('test_only', False),
                                                                       'dataset_keys': dataset_keys,
                                                                       'instances': [instance]},
                                                                 context={'request': request})

                        if not ledger_serializer.is_valid():
                            # delete instance
                            instance.delete()
                            raise ValidationError(ledger_serializer.errors)

                        # create on ledger
                        data, st = ledger_serializer.create(ledger_serializer.validated_data)

                        if st not in [status.HTTP_201_CREATED, status.HTTP_202_ACCEPTED]:
                            return Response(data, status=st)

                        headers = self.get_success_headers(serializer.data)
                        d = dict(serializer.data)
                        d.update(data)
                        return Response(d, status=st, headers=headers)

    @action(list=True)
    def update(self, request, *args, **kwargs):

        data = request.data
        dataset_keys = data.getlist('dataset_keys')
        data_keys = data.getlist('data_keys')

        serializer = self.get_serializer(Data.objects.filter(pkhash__in=data_keys), many=True)
        serializer.update()
        return Response(serializer.data)
