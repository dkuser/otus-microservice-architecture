# Generated by Django 3.2.9 on 2022-03-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactionapp', '0005_auto_20220325_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='user',
        ),
        migrations.AddField(
            model_name='balance',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
