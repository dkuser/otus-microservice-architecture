# Generated by Django 3.2.9 on 2022-03-25 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactionapp', '0004_remove_transaction_committed'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='balance',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='transactionapp.balance'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='order_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]