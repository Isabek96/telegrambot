import asyncio
import logging

from aiogram import Bot, Dispatcher
from app.config import token_api

# Роутеры
from app.handlers import router
from app.register import router as feedback_router

bot = Bot(token_api)
dp = Dispatcher()

# Запуск бота
async def main():
    # Подключаем оба роутера
    dp.include_router(router)
    dp.include_router(feedback_router)

    await dp.start_polling(bot)

# Запуск программы
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped!")
