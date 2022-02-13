from django.contrib import admin
from django.db import models, transaction
from rest_framework.exceptions import ValidationError


class CourierException(ValidationError):
    pass


class Courier(models.Model):
    is_free = models.BooleanField(default=True)


class Delivery(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.RESTRICT)
    order_id = models.IntegerField(unique=True)
    date = models.DateField()

    def save(self, *args, **kwargs) -> None:
        with transaction.atomic():
            courier = Courier.objects.filter(is_free=True).first()
            if courier is None:
                raise CourierException("Не хватает курьеров")
            courier.is_free = False
            self.courier = courier
            courier.save()
            super().save(*args, **kwargs)

    def rollback(self) -> None:
        with transaction.atomic():
            self.courier.is_free = True
            self.courier.save()
            self.delete()


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    pass


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    pass


@transaction.atomic()
def clean_database() -> None:
    Delivery.objects.all().delete()
    Courier.objects.all().delete()
