from django.contrib import admin
from django.db import models, transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from solo.models import SingletonModel


class TransactionException(ValidationError):
    pass


class Balance(SingletonModel):
    sum = models.IntegerField(default=0)


class Transaction(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    sum = models.IntegerField()
    order_id = models.IntegerField(unique=True)

    def save(self, *args, **kwargs) -> None:
        with transaction.atomic():
            balance = Balance.get_solo()
            balance.sum -= self.sum
            if balance.sum < 0:
                raise TransactionException("Не хватает денег")
            balance.save()
            super().save(*args, **kwargs)

    def rollback(self) -> None:
        with transaction.atomic():
            balance = Balance.get_solo()
            balance.sum += self.sum
            balance.save()
            self.delete()


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    pass


@transaction.atomic()
def clean_database() -> None:
    Balance.objects.all().delete()
    Transaction.objects.all().delete()
