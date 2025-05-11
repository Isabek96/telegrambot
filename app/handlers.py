# Импортируем библиотеку aiogram и объект Bot
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()

# Обработчик команды /start
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет, я бот!")

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Чтобы получить информацию о команде /help, напишите мне /help")

@router.message(F.text == "test")
async def cmd_test(message: Message):
    await message.answer("test")

@router.message(F.photo)
async def cmd_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')
  