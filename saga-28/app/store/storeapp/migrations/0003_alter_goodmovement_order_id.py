# Generated by Django 3.2.9 on 2022-02-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storeapp", "0002_alter_product_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goodmovement",
            name="order_id",
            field=models.IntegerField(unique=True),
        ),
    ]
