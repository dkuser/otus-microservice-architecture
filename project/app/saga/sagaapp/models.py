from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Order(models.Model):
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    sum = models.IntegerField(null=True)
    delivery_date = models.DateField()
    result = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=CASCADE)

    @property
    def success(self):
        return self.result is None


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'quantity', 'delivery_date', 'user', "success")
