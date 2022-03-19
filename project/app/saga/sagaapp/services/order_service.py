from typing import List

from sagaapp.models import Order
from .services import TransactionService, DeliveryService, StoreService, BaseService


class OrderService:
    SERVICES: List[BaseService] = [StoreService, TransactionService, DeliveryService]

    def __init__(self, order: Order) -> None:
        self.order = order

    def book(self) -> None:
        for service in self.SERVICES:
            service.book(self.order)

    def rollback(self) -> None:
        for service in self.SERVICES:
            service.rollback(self.order)
