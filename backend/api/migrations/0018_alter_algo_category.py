# Generated by Django 4.0.3 on 2022-05-31 14:00

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0017_alter_computeplan_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="algo",
            name="category",
            field=models.CharField(
                choices=[
                    ("ALGO_SIMPLE", "Algo Simple"),
                    ("ALGO_AGGREGATE", "Algo Aggregate"),
                    ("ALGO_COMPOSITE", "Algo Composite"),
                    ("ALGO_METRIC", "Algo Metric"),
                    ("ALGO_PREDICT", "Algo Predict"),
                ],
                max_length=64,
            ),
        ),
    ]
