import json
from typing import Any, Optional

from kafka import KafkaProducer

from sagaapp.models import Order
from settings import KAFKA_SERVER


def _value_serializer(value: Any) -> bytes:
    return json.dumps(value).encode("utf-8")


_producer: Optional[KafkaProducer] = None


def get_producer() -> KafkaProducer:
    global _producer
    if _producer is None:
        _producer = KafkaProducer(
            bootstrap_servers=KAFKA_SERVER, value_serializer=_value_serializer
        )
    return _producer


def emit_order(order: Order) -> None:
    if order.result is None:
        attributes = {
            "user_id": order.user.id,
            "item": f"Create new order {order.id} by user: {order.user.username}, product: {order.product_id} x {order.quantity} = {order.sum}",
        }
    else:
        attributes = {
            "user_id": order.user.id,
            "item": f"Fail new order {order.id} by user: {order.user.username}, product: {order.product_id} - {order.result}",
        }
    get_producer().send("logs", attributes)
    get_producer().flush()
