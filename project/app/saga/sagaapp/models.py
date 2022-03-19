from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    sum = models.IntegerField(null=True)
    delivery_date = models.DateField()
    result = models.TextField(null=True)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
