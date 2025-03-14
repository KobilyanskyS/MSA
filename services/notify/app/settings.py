# services/notify/app/settings.py
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

CONSUME_TOPIC = os.getenv("CURRENCY_TOPIC")

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")