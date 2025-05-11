from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import app.keyboards as kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f'Привет, {message.from_user.first_name} — Я ИИ-бот Южного Полевода. 🤖🌱\n'
        'Задай мне вопрос или выбери опцию ниже.\n\n'
        'Вот что я умею:\n'
        '✅ Подбор семян и удобрений\n'
        '✅ Консультации по уходу за культурами\n'
        '✅ Оформление заказов',
        reply_markup=kb.settings  # Ссылки
    )
    await message.answer("Главное меню:", reply_markup=kb.catalog_kb)  # Инлайн-кнопки с callback



@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Чтобы получить информацию о боте, напишите /start или выберите команду из меню.")


@router.message(F.text.lower() == "привет")
async def greeting_1(message: Message):
    await message.answer("Привет!")


@router.message(F.text.lower() == "здравствуйте")
async def greeting_2(message: Message):
    await message.answer("Здравствуйте!")


@router.callback_query(F.data == "catalog")
async def cmd_catalog(callback: CallbackQuery):
    await callback.message.edit_text("Выберите семена и удобрения из каталога.", reply_markup=await kb.inline_menu_1())
    await callback.answer('Вы выбрали каталог')  # Не забудь закрыть callback
