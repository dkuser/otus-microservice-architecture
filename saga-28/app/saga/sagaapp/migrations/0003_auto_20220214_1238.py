# Generated by Django 3.2.9 on 2022-02-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sagaapp", "0002_admin"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="committed_delivery",
        ),
        migrations.RemoveField(
            model_name="order",
            name="committed_store",
        ),
        migrations.RemoveField(
            model_name="order",
            name="committed_transaction",
        ),
        migrations.AddField(
            model_name="order",
            name="result",
            field=models.JSONField(null=True),
        ),
    ]
