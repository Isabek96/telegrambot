from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()


class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(Command("start"))
async def cmd_start(message: Message):
    # Прямая ссылка на GIF
    gif_url = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExam9jY2E3M2tkb2VyOW5hNHBlZGx5OWVneW10dm5vYWJlZXJzMDRzeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/u8BOqJz4hRQJj8fBMz/giphy.gif"

    # Отправка GIF с внешней ссылки
    await message.answer_animation(gif_url)

    # Отправка текста
    await message.answer(
        f'Привет, {message.from_user.first_name} — Я ИИ-бот Южного Полевода. 🤖🌱\n'
        'Задай мне вопрос или выбери опцию ниже.\n\n'
        'Вот что я умею:\n'
        '✅ Подбор семян и удобрений\n'
        '✅ Консультации по уходу за культурами\n'
        '✅ Оформление заказов',
        reply_markup=kb.settings
    )

    await message.answer("Главное меню:", reply_markup=kb.catalog_kb)


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Чтобы получить информацию о боте, напишите /start или выберите команду из меню.")


@router.message(F.text.lower() == "привет")
async def greeting_1(message: Message):
    await message.answer("Привет!")


@router.message(F.text.lower() == "здравствуйте")
async def greeting_2(message: Message):
    await message.answer("Здравствуйте!")


# Контакты
@router.callback_query(F.data == 'contacts')
async def cmd_contact(callback: CallbackQuery):
    await callback.message.edit_text('Выберите город:', reply_markup=await kb.inline_contact())
    await callback.answer()


@router.callback_query(F.data == 'city_Алматы')
async def cmd_contact_alma(callback: CallbackQuery):
    await callback.message.edit_text('Номера телефонов', reply_markup=await kb.contact_number_almaty())
    await callback.answer()


# Каталог товаров
@router.callback_query(F.data == "catalog")
async def cmd_catalog(callback: CallbackQuery):
    await callback.message.edit_text("Выберите семена и удобрения из каталога.", reply_markup=await kb.inline_menu_1())
    await callback.answer('Вы выбрали каталог')  # Не забудь закрыть callback


@router.callback_query(F.data == "Открытый грунт")
async def show_otkrytyj_grunt(callback: CallbackQuery):
    await callback.message.edit_text("Выберите категорию из открытого грунта:",
                                     reply_markup=await kb.inline_menu_otk_grunt())
    await callback.answer()


@router.callback_query(F.data == "Закрытый грунт")
async def show_zaktiti_grunt(callback: CallbackQuery):
    await callback.message.edit_text("Выберите категорию из Закрытого грунта:",
                                     reply_markup=await kb.inline_menu_zakr_grunt())
    await callback.answer()


@router.callback_query(F.data == 'Удобрения')
async def show_zaktiti(callback: CallbackQuery):
    await callback.message.edit_text("Выберите семена и удобрения из каталога.",
                                     reply_markup=await kb.inline_menu_udobrenie())
    await callback.answer()


# Назад к каталогу
@router.callback_query(F.data == "back_to_catalog")
async def back_to_catalog(callback: CallbackQuery):
    await callback.message.edit_text("Выберите семена и удобрения из каталога.", reply_markup=await kb.inline_menu_1())
    await callback.answer()


# Главное меню
@router.callback_query(F.data == "go_home")
async def go_home(callback: CallbackQuery):
    await callback.message.edit_text("Вы вернулись в главное меню.", reply_markup=kb.catalog_kb)
    await callback.answer()


# Регистрация клиентов
@router.message(Command('reg'))
async def cmd_register(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите Ваше Имя')


@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer(('Введите номер телефона'))


@router.message(Reg.number)
async def reg_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо, регистрация завершена\nИмя:{data["name"]}\nНомер:{data["number"]}')
    await state.clear()
