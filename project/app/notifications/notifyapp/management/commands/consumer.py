import json
import logging

from django.core.management.base import BaseCommand
from kafka import KafkaConsumer

from notifyapp.models import Log
from settings import KAFKA_SERVER


def _value_deserializer(value: bytes) -> dict:
    return json.loads(value.decode("utf-8"))


class Command(BaseCommand):
    help = "Kafka consumer"

    def handle(self, *args, **options):
        consumer = KafkaConsumer(
            "logs",
            bootstrap_servers=[KAFKA_SERVER],
            value_deserializer=_value_deserializer,
            auto_offset_reset="earliest",
        )

        logging.info("start")
        for message in consumer:
            logging.info(message)
            Log.objects.create(**message.value)
