# Generated by Django 4.0.3 on 2022-04-21 15:23

from django.db import migrations


def convert_address(apps, schema_editor):
    metric_model = apps.get_model("substrapp", "metric")
    for metric in metric_model.objects.all():
        metric.file.name = metric.file.name.replace("metrics/", "algos/")
        metric.description.name = metric.description.name.replace("metrics/", "algos/")
        metric.save()


def copy_from_metric_to_algo(apps, schema_editor):
    metric_model = apps.get_model("substrapp", "metric")
    algo_model = apps.get_model("substrapp", "algo")

    for metric in metric_model.objects.all().values():
        algo_model.objects.create(**metric)


class Migration(migrations.Migration):

    dependencies = [
        ("substrapp", "0008_alter_imageentrypoint_entrypoint_json"),
    ]

    operations = [
        migrations.RenameField(model_name="metric", old_name="address", new_name="file"),
        migrations.RemoveField(model_name="metric", name="creation_date"),
        migrations.RemoveField(model_name="metric", name="last_modified"),
        migrations.RunPython(convert_address),
        migrations.RunPython(copy_from_metric_to_algo),
        migrations.DeleteModel(
            name="Metric",
        ),
    ]
