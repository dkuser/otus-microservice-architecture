import json
import logging
import traceback
from time import sleep

from django.core.management.base import BaseCommand
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

from notifyapp.models import Log
from settings import KAFKA_SERVER


def _value_deserializer(value: bytes) -> dict:
    return json.loads(value.decode("utf-8"))


class Command(BaseCommand):
    help = "Kafka consumer"

    def get_consumer(self) -> KafkaConsumer:
        while True:
            try:
                return KafkaConsumer(
                    "logs",
                    bootstrap_servers=[KAFKA_SERVER],
                    value_deserializer=_value_deserializer,
                    auto_offset_reset="earliest",
                )
            except NoBrokersAvailable:
                traceback.print_exc()
                sleep(1)

    def handle(self, *args, **options):
        consumer = self.get_consumer()

        logging.info("start")
        for message in consumer:
            logging.info(message)
            Log.objects.create(**message.value)
