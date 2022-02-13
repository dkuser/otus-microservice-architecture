# Generated by Django 3.2.9 on 2022-02-13 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_id", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("sum", models.IntegerField()),
                ("delivery_date", models.DateField()),
                ("committed_transaction", models.BooleanField(default=False)),
                ("committed_store", models.BooleanField(default=False)),
                ("committed_delivery", models.BooleanField(default=False)),
            ],
        ),
    ]