from django.contrib import admin
from django.core.cache import cache
from django.db import models, transaction


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    item = models.CharField(max_length=200, blank=False)
    cost = models.IntegerField()
    quantity = models.IntegerField()

    def save(self, *args, **kwargs) -> None:
        cache.clear()
        super().save(*args, **kwargs)


@transaction.atomic()
def clean_database() -> None:
    Product.objects.all().delete()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
