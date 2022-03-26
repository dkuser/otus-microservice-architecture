from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models, transaction
from django.db.models import CASCADE
from django.db.transaction import atomic
from django.utils import timezone
from rest_framework.exceptions import ValidationError


class TransactionException(ValidationError):
    pass


class Balance(models.Model):
    user_id = models.IntegerField(default=0)
    sum = models.IntegerField(default=0)


class Transaction(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    sum = models.IntegerField()
    order_id = models.IntegerField(unique=True, null=True)
    balance = models.ForeignKey(Balance, on_delete=CASCADE)

    def save(self, *args, **kwargs) -> None:
        with transaction.atomic():
            self.balance.sum += self.sum
            if self.balance.sum < 0:
                raise TransactionException("Не хватает денег")
            self.balance.save()
            super().save(*args, **kwargs)

    def rollback(self) -> None:
        with transaction.atomic():
            self.balance.sum -= self.sum
            self.balance.save()
            self.delete()

    @atomic
    def save_with_user(self, user_id: int) -> None:
        balance, _ = Balance.objects.get_or_create(user_id=user_id, defaults={"sum": 0})
        self.balance = balance
        self.save()


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
