# services/currency/currency/settings.py
import os

# --- SCRAPY SETTINGS

BOT_NAME = "currency"
SPIDER_MODULES = ["currency.spiders"]
NEWSPIDER_MODULE = "currency.spiders"
ROBOTSTXT_OBEY = True
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# --- REDIS SETTINGS

CURRENCY_REDIS_CACHE_TIME_IN_SECONDS = 60

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"

# --- KAFKA SETTINGS

PRODUCE_TOPIC = os.getenv("CURRENCY_TOPIC")
CONSUME_TOPIC = os.getenv("WEB_TOPIC")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")