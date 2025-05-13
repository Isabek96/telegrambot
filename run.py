import asyncio
import logging

# Импортируем библиотеку aiogram и объект Bot
from aiogram import Bot, Dispatcher

from app.handlers import router
from config import token_api

bot = Bot(token_api)
dp = Dispatcher()


# Запуск бота
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)  # передаем bot в функцию start_polling


# Запуск программы
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped!")
