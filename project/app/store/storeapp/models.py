from django.contrib import admin
from django.db import models, transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError


class StoreException(ValidationError):
    pass


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    item = models.CharField(max_length=200, blank=False)
    cost = models.IntegerField()
    quantity = models.IntegerField()


class GoodMovement(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    order_id = models.IntegerField(unique=True)
    sum = models.IntegerField()

    def save(self, *args, **kwargs) -> None:
        with transaction.atomic():
            self.product.quantity -= self.quantity
            if self.product.quantity < 0:
                raise StoreException("Не хватает товара")
            self.product.save()
            self.sum = self.quantity * self.product.cost
            super().save(*args, **kwargs)

    def rollback(self) -> None:
        with transaction.atomic():
            self.product.quantity += self.quantity
            self.product.save()
            self.delete()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(GoodMovement)
class GoodMovementAdmin(admin.ModelAdmin):
    pass


@transaction.atomic()
def clean_database() -> None:
    GoodMovement.objects.all().delete()
    Product.objects.all().delete()
