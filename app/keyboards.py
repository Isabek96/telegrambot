from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


# Главное меню (обычные кнопки)
catalog_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Подбор семян и удобрений", callback_data="catalog")],
    [InlineKeyboardButton(text="Корзина", callback_data="cart")],
    [InlineKeyboardButton(text="Контакты", callback_data="contacts")],
    [InlineKeyboardButton(text="Обратная связь", callback_data="feedback")],
])





# Инлайн-кнопка со ссылкой
settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Наш сайт", url="https://polevod.com")],
        [InlineKeyboardButton(text="ТикТок канал", url="https://www.tiktok.com/@polevodtv")],
         [InlineKeyboardButton(text="Youtube канал", url="https://www.youtube.com/c/PolevodTV")]
    ]
)


# Список для динамического создания обычных кнопок
menu_1 = ['Открытый грунт', 'Закрытый грунт', 'Удобрения','Семена люцерны']

# Функция для создания клавиатуры (Reply, не Inline)
# Функция для создания инлайн-кнопок
async def inline_menu_1():
    builder = InlineKeyboardBuilder()
    for men in menu_1:
        builder.add(InlineKeyboardButton(text=men, callback_data=men))
    return builder.adjust(2).as_markup()
