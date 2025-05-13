from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

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

# Конпка для контакты
contacty_kb = ['Алматы', 'Шымкент']


async def inline_contact():
    builder = InlineKeyboardBuilder()
    for city in contacty_kb:
        builder.add(InlineKeyboardButton(
            text=city,
            callback_data=f"city_{city}"
        ))
    builder.adjust(2)
    builder.row(
        InlineKeyboardButton(text='⬅️ назад', callback_data='go_home'),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="go_home")
    )
    return builder.as_markup()


async def contact_number_almaty():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="+77012261483", callback_data="phone_1"))
    builder.add(InlineKeyboardButton(text="+77010292199", callback_data="phone_2"))
    builder.adjust(2)  # Примерная настройка для удобства отображения
    return builder.as_markup()


# Inline кнопки для каталога
# Список для динамического создания обычных кнопок
menu_1 = ['Открытый грунт', 'Закрытый грунт', 'Удобрения', 'Семена люцерны']


# Функция для создания клавиатуры (Reply, не Inline)
# Функция для создания инлайн-кнопок
async def inline_menu_1():
    builder = InlineKeyboardBuilder()
    for men in menu_1:
        builder.add(InlineKeyboardButton(text=men, callback_data=men))

    builder.adjust(2)

    builder.row(
        InlineKeyboardButton(text='⬅️ назад', callback_data='go_home'),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="go_home")
    )
    return builder.as_markup()


otk_grunt = ['Томаты', 'Огурец', 'Морковь', 'Капуста', 'Цветная капуста', 'Пекинская капуста',
             'Краснокочанная капуста', 'Арбуз', 'Дыня', 'Свекла', 'Кукуруза сладкая',
             'Баклажан', 'Сладкий перец', 'Острый перец', 'Лук', 'Кабачок',
             'Редис', 'Тыква', 'Брокколи', 'Зелень', 'Шпинаты']


async def inline_menu_otk_grunt():
    builder = InlineKeyboardBuilder()
    for men_otk_grunt in otk_grunt:
        builder.add(InlineKeyboardButton(text=men_otk_grunt, callback_data=men_otk_grunt))
    builder.adjust(2)
    builder.row(
        InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_catalog"),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="go_home")
    )

    return builder.as_markup()


zak_grunt = ['Томаты', 'Огурец', 'Баклажан', 'Сладкий перец', 'Острый перец',
             'Брокколи', 'Зелень']


async def inline_menu_zakr_grunt():
    builder = InlineKeyboardBuilder()
    for men_zak_grunt in zak_grunt:
        builder.add(InlineKeyboardButton(text=men_zak_grunt, callback_data=men_zak_grunt))
    builder.adjust(2)

    builder.row(
        InlineKeyboardButton(text='⬅️ назад', callback_data='back_to_catalog'),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="go_home")
    )
    return builder.as_markup()


udobrenie = ['Простые', 'Комплексные', 'Аминокислотные', 'Гуминовые', 'Микроэлементы']


async def inline_menu_udobrenie():
    builder = InlineKeyboardBuilder()
    for men_udobrene in udobrenie:
        builder.add(InlineKeyboardButton(text=men_udobrene, callback_data=men_udobrene))
    builder.adjust(2)
    builder.row(
        InlineKeyboardButton(text='⬅️ назад', callback_data='back_to_catalog'),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="go_home")
    )
    return builder.as_markup()
