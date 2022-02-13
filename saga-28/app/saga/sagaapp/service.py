import traceback

import requests
from django.db.transaction import atomic
from requests import RequestException, HTTPError
from rest_framework.exceptions import ValidationError

from sagaapp.models import Order
from settings import STORE_SERVICE, TRANSACTION_SERVICE, DELIVERY_SERVICE


@atomic
def book_order(order: Order) -> Order:
    order.save()
    try:
        book_store(order)
        book_transaction(order)
        book_delivery(order)
    except ValidationError as e:
        order.result = str(e)
        order.save()
    return order


def book_store(order: Order) -> None:
    params = {
        "product": order.product_id,
        "quantity": order.quantity,
        "order_id": order.id,
    }
    result = _book_in_service(STORE_SERVICE, params)
    order.sum = result["sum"]
    order.save()


def book_transaction(order: Order) -> None:
    params = {"sum": order.sum, "order_id": order.id}
    _book_in_service(TRANSACTION_SERVICE, params)


def book_delivery(order: Order) -> None:
    params = {"date": order.delivery_date, "order_id": order.id}
    _book_in_service(DELIVERY_SERVICE, params)


def _book_in_service(service_host: str, params: dict) -> dict:
    try:
        response = requests.post(f"{service_host}/books/", params)
        response.raise_for_status()
    except HTTPError as e:
        traceback.print_exc()
        raise ValidationError(f"Error in {service_host}: {e.response.text}")
    except RequestException:
        traceback.print_exc()
        raise ValidationError(f"Error in {service_host}")
    return response.json()
