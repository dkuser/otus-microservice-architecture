# Generated by Django 3.2.9 on 2022-02-13 05:35

from django.db import migrations
from core import init_migrations


class Migration(migrations.Migration):

    dependencies = [
        ("deliveryapp", "0002_remove_delivery_committed"),
    ]

    def forwards_func(apps, schema_editor):
        init_migrations()

    operations = [
        migrations.RunPython(forwards_func),
    ]
