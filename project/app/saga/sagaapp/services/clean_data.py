from sagaapp.models import Order
from .services import TransactionService, DeliveryService, StoreService


def clean_data() -> None:
    Order.objects.all().delete()
    DeliveryService.flush()
    TransactionService.flush()
    StoreService.flush()
