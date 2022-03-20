from django.contrib import admin
from django.db import models, transaction


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    item = models.CharField(max_length=200, blank=False)
    cost = models.IntegerField()
    quantity = models.IntegerField()


@transaction.atomic()
def clean_database() -> None:
    Product.objects.all().delete()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

