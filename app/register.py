from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import re
import app.keyboards as kb
from database import get_connection

router = Router()

class Feedback(StatesGroup):
    name = State()
    number = State()

# При нажатии на кнопку "Обратная связь"
@router.callback_query(F.data == "feedback")
async def feedback_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Feedback.name)
    await callback.message.answer("Пожалуйста, введите ваше имя:")
    await callback.answer()

# Получаем имя
@router.message(Feedback.name)
async def feedback_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Feedback.number)
    await message.answer("Введите ваш номер телефона:")


@router.message(Feedback.number)
async def feedback_number(message: Message, state: FSMContext):
    phone_number = message.text
    if not re.match(r"^\+?\d{10,15}$", phone_number):
        await message.answer("Пожалуйста, введите корректный номер телефона.")
        return

    await state.update_data(number=phone_number)
    data = await state.get_data()

    # Сохраняем в базу
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO feedback (name, phone) VALUES (%s, %s)",
            (data['name'], data['number'])
        )
        conn.commit()

    await message.answer(f"Спасибо! Мы свяжемся с вами:\n\nИмя: {data['name']}\nТелефон: {data['number']}")
    await state.clear()
@router.callback_query(F.data == 'back_go_cato')
async def go_back_to_catalog(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Вы вернулись в каталог.", reply_markup=await kb.setting_inline)
    await callback.answer()

@router.callback_query(F.data == 'city_Алматы')
async def cmd_contact_alma(callback: CallbackQuery):
    await callback.message.edit_text('Номера телефонов', reply_markup=await kb.contact_number_almaty())
    await callback.answer()

