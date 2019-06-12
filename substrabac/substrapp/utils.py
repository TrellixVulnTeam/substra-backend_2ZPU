
import io
import hashlib
import logging
import os
import tempfile
from os.path import isfile, isdir

import requests
import tarfile
import zipfile

from checksumdir import dirhash

from django.conf import settings
from rest_framework import status


class JsonException(Exception):
    def __init__(self, msg):
        self.msg = msg
        super(JsonException, self).__init__()


def get_dir_hash(archive_content):
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            content = archive_content.read()
            archive_content.seek(0)
            uncompress_content(content, temp_dir)
        except Exception as e:
            logging.error(e)
            raise e
        else:
            return dirhash(temp_dir, 'sha256')


def get_hash(file, key=None):
    if file is None:
        return ''
    else:
        if isinstance(file, (str, bytes, os.PathLike)):
            if isfile(file):
                with open(file, 'rb') as f:
                    data = f.read()
            elif isdir(file):
                return dirhash(file, 'sha256')
            else:
                return ''
        else:
            openedfile = file.open()
            data = openedfile.read()
            openedfile.seek(0)

        return compute_hash(data, key)


def compute_hash(bytes, key=None):
    sha256_hash = hashlib.sha256()

    if isinstance(bytes, str):
        bytes = bytes.encode()

    if key is not None and isinstance(key, str):
        bytes += key.encode()

    sha256_hash.update(bytes)

    return sha256_hash.hexdigest()


def get_computed_hash(url, key=None):
    response = get_from_node(url)
    computedHash = compute_hash(response.content, key)

    return response.content, computedHash


def get_remote_file(object, key=None):
    content, computed_hash = get_computed_hash(object['storageAddress'], key)

    if computed_hash != object['hash']:
        msg = 'computed hash is not the same as the hosted file.' \
              'Please investigate for default of synchronization, corruption, or hacked'
        raise Exception(msg)

    return content, computed_hash


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def uncompress_path(archive_path, to_directory):
    if zipfile.is_zipfile(archive_path):
        zip_ref = zipfile.ZipFile(archive_path, 'r')
        zip_ref.extractall(to_directory)
        zip_ref.close()
    elif tarfile.is_tarfile(archive_path):
        tar = tarfile.open(archive_path, 'r:*')
        tar.extractall(to_directory)
        tar.close()
    else:
        raise Exception('Archive must be zip or tar.gz')


def uncompress_content(archive_content, to_directory):
    if zipfile.is_zipfile(io.BytesIO(archive_content)):
        zip_ref = zipfile.ZipFile(io.BytesIO(archive_content))
        zip_ref.extractall(to_directory)
        zip_ref.close()
    else:
        try:
            tar = tarfile.open(fileobj=io.BytesIO(archive_content))
            tar.extractall(to_directory)
            tar.close()
        except tarfile.TarError:
            raise Exception('Archive must be zip or tar.*')


class NodeError(Exception):
    pass


def get_from_node(url):

    kwargs = {
        'headers': {'Accept': 'application/json;version=0.0'},
    }

    username = getattr(settings, 'BASICAUTH_USERNAME', None)
    password = getattr(settings, 'BASICAUTH_PASSWORD', None)
    if username is not None and password is not None:
        kwargs['auth'] = (username, password)

    if settings.DEBUG:
        kwargs['verify'] = False

    try:
        response = requests.get(url, **kwargs)
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        raise NodeError(f'Failed to fetch {url}') from e
    else:
        if response.status_code != status.HTTP_200_OK:
            logging.error(response.text)
            raise NodeError(f'Url: {url} returned status code: {response.status_code}')

    return response
