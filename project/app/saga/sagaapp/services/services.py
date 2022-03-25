import abc
import traceback
from typing import Any

import requests
from requests import RequestException, HTTPError, Response
from rest_framework.exceptions import ValidationError

from sagaapp.models import Order
from settings import STORE_SERVICE, TRANSACTION_SERVICE, DELIVERY_SERVICE, ROOT_TOKEN


class BaseService(abc.ABC):
    url: str
    prefix: str

    @classmethod
    def _request(
        cls, method: str, path: str, raise_for_status: bool = True, **kwargs: Any
    ) -> Response:
        try:
            headers = {"Authorization": f"Token {ROOT_TOKEN}"}
            response = requests.request(
                method, f"{cls.url}/{cls.prefix}{path}", headers=headers, **kwargs
            )
            if raise_for_status:
                response.raise_for_status()
        except HTTPError as e:
            traceback.print_exc()
            raise ValidationError(f"Error in {cls.url}: {e.response.text}") from e
        except RequestException as e:
            traceback.print_exc()
            raise ValidationError(f"Error in {cls.url}") from e
        return response

    @classmethod
    def flush(cls) -> None:
        cls._request("post", "flush/", data={})

    @classmethod
    @abc.abstractmethod
    def book(cls, order: Order) -> None:
        pass

    @classmethod
    def rollback(cls, order: Order) -> None:
        response = cls._request("delete", f"orders/{order.id}/", raise_for_status=False)
        if response.status_code == 404:
            return
        response.raise_for_status()

    @classmethod
    def _book_in_service(cls, params: dict) -> dict:
        response = cls._request("post", "books/", data=params)
        return response.json()


class TransactionService(BaseService):
    url = TRANSACTION_SERVICE
    prefix = "transaction/"

    @classmethod
    def book(cls, order: Order) -> None:
        params = {"sum": order.sum, "order_id": order.id}
        cls._book_in_service(params)


class StoreService(BaseService):
    url = STORE_SERVICE
    prefix = "store/"

    @classmethod
    def book(cls, order: Order) -> None:
        params = {
            "product": order.product_id,
            "quantity": order.quantity,
            "order_id": order.id,
        }
        result = cls._book_in_service(params)
        order.sum = result["sum"]
        order.save()


class DeliveryService(BaseService):
    url = DELIVERY_SERVICE
    prefix = "delivery/"

    @classmethod
    def book(cls, order: Order) -> None:
        params = {"date": order.delivery_date, "order_id": order.id}
        cls._book_in_service(params)
