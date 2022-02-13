# Generated by Django 3.2.9 on 2022-02-13 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Courier",
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
                ("is_free", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Delivery",
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
                ("order_id", models.IntegerField(unique=True)),
                ("date", models.DateField()),
                ("committed", models.BooleanField(default=False)),
                (
                    "courier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="deliveryapp.courier",
                    ),
                ),
            ],
        ),
    ]