from typing import List

from rest_framework.exceptions import ValidationError

from sagaapp.models import Order
from .events import emit_order
from .services import TransactionService, DeliveryService, StoreService, BaseService


class OrderService:
    SERVICES: List[BaseService] = [StoreService, TransactionService, DeliveryService]

    def __init__(self, order: Order) -> None:
        self.order = order

    def book(self) -> None:
        self.order.save()
        try:
            for service in self.SERVICES:
                service.book(self.order)
        except ValidationError as e:
            self.order.result = str(e)
            self.order.save()
        emit_order(self.order)

    def rollback(self) -> None:
        for service in self.SERVICES:
            service.rollback(self.order)
