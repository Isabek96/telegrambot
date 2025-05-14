from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder



# Главное меню (обычные кнопки)
catalog_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌱 Подбор семян и удобрений", callback_data="catalog")],
    [InlineKeyboardButton(text="🛒 Корзина", callback_data="cart")],
    [InlineKeyboardButton(text="📞 Контакты", callback_data="contacts")],
    [InlineKeyboardButton(text="✉️ Обратная связь", callback_data="feedback")],
    [InlineKeyboardButton(text="⚙️ Настройки", callback_data="setting_1")]
])

# Инлайн-кнопка со ссылкой
settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌐 Наш сайт", url="https://polevod.com")],
        [InlineKeyboardButton(text="🎵 ТикТок канал", url="https://www.tiktok.com/@polevodtv")],
        [InlineKeyboardButton(text="📺 YouTube канал", url="https://www.youtube.com/c/PolevodTV")],
        [InlineKeyboardButton(text="🛍️ Каспий магазин", url="https://kaspi.kz/shop/p/arbuz-au-prodjuser---au-producer-132404656/?c=511010000")],
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


# Контакты Алматы
async def contact_number_almaty():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="+77012261483", callback_data="phone_1"))
    builder.add(InlineKeyboardButton(text="+77010292199", callback_data="phone_2"))
    builder.adjust(2)  # Примерная настройка для удобства отображения
    builder.row(
        InlineKeyboardButton(text='⬅️ назад', callback_data='back_go_cato'),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="go_home")
    )
    return builder.as_markup()


# Конакты Шымкент
async def contact_number_shymkent():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="+77017831267 ", callback_data="phone_3"))
    builder.add(InlineKeyboardButton(text="+77052838572", callback_data="phone_4"))
    builder.adjust(2)  # Примерная настройка для удобства отображения
    builder.row(
        InlineKeyboardButton(text='⬅️ назад', callback_data='back_go_cato'),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="go_home")
    )
    return builder.as_markup()




#Обратная связь

#Настройки

async def setting_inline():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='Имя', callback_data='name_register'))
    builder.add(InlineKeyboardButton(text='Фамилия', callback_data='familya_register'))
    builder.add(InlineKeyboardButton(text='Номер телефона', callback_data='phone_register'))
    builder.add(InlineKeyboardButton(text='Город', callback_data='city_register'))
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text='🔔 Уведомления', callback_data='uvedomlenye_register'))
    builder.row(
        InlineKeyboardButton(text='⬅️ Назад', callback_data='go_home'),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="go_home")
    )
    return builder.as_markup()





# Inline кнопки для каталога
# Список для динамического создания обычных кнопок
menu_1 = ['Открытый грунт', 'Закрытый грунт', 'Удобрения', 'Семена люцерны']


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


otk_grunt = [    ("🍅 Томаты"), ("🥒 Огурец"), ("🥕 Морковь"), ("🥬 Капуста"),
    ("🥦 Цветная капуста"), ("🥬 Пекинская капуста"), ("🥬 Краснокочанная капуста"),
    ("🍉 Арбуз"), ("🍈 Дыня"), ("🧃 Свекла"), ("🌽 Кукуруза сладкая"),
    ("🍆 Баклажан"), ("🫑 Сладкий перец"), ("🌶️ Острый перец"), ("🧅 Лук"),
    ("🥒 Кабачок"), ("🌱 Редис"), ("🎃 Тыква"), ("🥦 Брокколи"),
    ("🌿 Зелень"), ("🌿 Шпинаты")]

async def inline_menu_otk_grunt():
    builder = InlineKeyboardBuilder()
    for men_otk_grunt in otk_grunt:
        builder.add(InlineKeyboardButton(text=men_otk_grunt, callback_data=f"item_{men_otk_grunt}"))
    builder.adjust(2)

    builder.row(
        InlineKeyboardButton(text='⬅️ назад', callback_data='back_to_catalog'),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="go_home")
    )
    return builder.as_markup()



zakr_grunt = ["🥬 Салат", "🌿 Базилик", "🧄 Чеснок"]
udobrenie = ["Комплексное", "Азотное", "Фосфорное", "Калийное"]

async def inline_menu_zakr_grunt():
    builder = InlineKeyboardBuilder()
    for item in zakr_grunt:
        builder.add(InlineKeyboardButton(text=item, callback_data=f"item_{item}"))
    builder.adjust(2)
    builder.row(
        InlineKeyboardButton(text='⬅️ назад', callback_data='back_to_catalog'),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="go_home")
    )
    return builder.as_markup()


async def inline_menu_udobrenie():
    builder = InlineKeyboardBuilder()
    for item in udobrenie:
        builder.add(InlineKeyboardButton(text=item, callback_data=f"item_{item}"))
    builder.adjust(2)
    builder.row(
        InlineKeyboardButton(text='⬅️ назад', callback_data='back_to_catalog'),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="go_home")
    )
    return builder.as_markup()

