# Generated by Django 3.2.9 on 2022-02-13 05:35

from django.db import migrations
from core import init_migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactionapp", "0006_auto_20220325_1224"),
    ]

    def forwards_func(apps, schema_editor):
        init_migrations()

    operations = [
        migrations.RunPython(forwards_func),
    ]
