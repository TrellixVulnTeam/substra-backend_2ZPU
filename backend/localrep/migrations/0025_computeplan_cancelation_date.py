# Generated by Django 4.0.6 on 2022-07-22 12:19

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("localrep", "0024_computetaskinput"),
    ]

    operations = [
        migrations.AddField(
            model_name="computeplan",
            name="cancelation_date",
            field=models.DateTimeField(null=True),
        ),
    ]
