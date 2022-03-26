from django.contrib import admin
from django.db import models, transaction


class Log(models.Model):
    item = models.TextField(blank=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


@transaction.atomic()
def clean_database() -> None:
    Log.objects.all().delete()


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    pass
