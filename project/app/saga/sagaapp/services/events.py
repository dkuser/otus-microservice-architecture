import json
from typing import Any

from django.forms import model_to_dict
from kafka import KafkaProducer

from sagaapp.models import Order
from settings import KAFKA_SERVER


def _value_serializer(value: Any) -> bytes:
    return json.dumps(value).encode("utf-8")


_producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER, value_serializer=_value_serializer
)


def emit_order(order: Order) -> None:
    if order.result is None:
        attributes = {
            "user_id": 0,
            "item": f"Create new order {order.id}, product: {order.product_id} x {order.quantity} = {order.sum}",
        }
    else:
        attributes = {
            "user_id": 0,
            "item": f"Fail new order {order.id}, product: {order.product_id} - {order.result}",
        }
    _producer.send("logs", attributes)
    _producer.flush()
