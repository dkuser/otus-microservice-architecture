import decimal

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models, transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError


class User(AbstractUser):
    balance = models.DecimalField(blank=False, default=0, max_digits=30, decimal_places=2)


class TransactionException(ValidationError):
    pass


class Transaction(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sum = models.DecimalField(blank=False, max_digits=30, decimal_places=2)

    def save(self, *args, **kwargs) -> None:
        with transaction.atomic():
            user = User.objects.filter(id=self.user.id).select_for_update().get()
            user.balance += self.sum
            if user.balance < 0:
                raise TransactionException("Не хватает денег")
            user.save()
            super().save(*args, **kwargs)


class Order(models.Model):
    item = models.CharField(max_length=200, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.DecimalField(blank=False, max_digits=30, decimal_places=2, validators=[MinValueValidator(0)])
    request_id = models.UUIDField(unique=True)

    @transaction.atomic()
    def save(self, *args, **kwargs) -> None:
        self.user.transaction_set.create(sum=-self.cost)
        super().save(*args, **kwargs)
