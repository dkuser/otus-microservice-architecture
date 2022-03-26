from django.contrib.auth.models import User

from sagaapp.models import Order
from .services import (
    TransactionService,
    DeliveryService,
    StoreService,
    NotificationService,
    FinerService,
)


def clean_data() -> None:
    Order.objects.all().delete()
    DeliveryService.flush()
    TransactionService.flush()
    StoreService.flush()
    NotificationService.flush()
    FinerService.flush()
    User.objects.filter(is_superuser=False).delete()
