from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters.command import Command
from aiokafka import AIOKafkaConsumer
from notify.app import settings
from notify.app.keyboard import get_kb

import aiohttp
import asyncio
import json

dispatcher = Dispatcher()
BOT = Bot(token=settings.BOT_TOKEN)


@dispatcher.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Выберите необходимую валюту", reply_markup=get_kb())

@dispatcher.callback_query()
async def process_currency_button(callback_query: types.CallbackQuery):
    currency_char_code = callback_query.data
    telegram_id = callback_query.from_user.id

    async with aiohttp.ClientSession() as session:
        async with session.post(
            "http://web:8000/currency-info",
            json={
                "currency_char_code": currency_char_code,
                "telegram_id": int(telegram_id)
            },
            headers={
                "Content-Type": "application/json"
            }
        ) as response:
            if response.status == 200:
                await callback_query.answer("Запрос успешно отправлен!")
            else:
                await callback_query.answer("Ошибка при отправке запроса.")

    await callback_query.answer()



async def consume() -> None:
    consumer = AIOKafkaConsumer(
        settings.CONSUME_TOPIC,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
    )
    await consumer.start()
    try:
        async for msg in consumer:
            serialized = json.loads(msg.value)
            await BOT.send_message(
                chat_id=serialized.get("telegram_id"),
                text=serialized.get("currency_value") or "Валюта не найдена",
            )
    finally:
        await consumer.stop()

async def main() -> None:
    polling = asyncio.create_task(dispatcher.start_polling(BOT))
    consuming = asyncio.create_task(consume())
    await asyncio.gather(polling, consuming)
    print("Bot has successfully started polling")


if __name__ == "__main__":
    asyncio.run(main())