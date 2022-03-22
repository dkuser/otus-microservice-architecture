import json
from typing import Any

from django.forms import model_to_dict
from kafka import KafkaProducer

from settings import KAFKA_SERVER
from storeapp.models import Product


def _value_serializer(value: Any) -> bytes:
    return json.dumps(value).encode("utf-8")


_producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER, value_serializer=_value_serializer
)


def emit_change_product(product: Product) -> None:
    attributes = model_to_dict(product)
    _producer.send("products", attributes)
    _producer.flush()
