from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_keyboard():
    menu_keyboard = [
        [
            InlineKeyboardButton(text="Оплатить Доступ", callback_data="pay_access"),
        ],
        [
            InlineKeyboardButton(text="Подарить доступ", callback_data="gift_access"),
            InlineKeyboardButton(text="Подробнее о канале", callback_data="about_channel")
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=menu_keyboard, resize_keyboard=True)


def subscription_duration_keyboard():
    keyboard = [
        [InlineKeyboardButton(text="1 месяц", callback_data="subscribe_1")],
        [InlineKeyboardButton(text="6 месяцев", callback_data="subscribe_6")],
        [InlineKeyboardButton(text="12 месяцев", callback_data="subscribe_12")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True)

def payment_method_keyboard():
    keyboard = [
        [InlineKeyboardButton(text="Оплата Telegram Stars", callback_data="pay_stars")],
        [InlineKeyboardButton(text="Оплата USDT", callback_data="pay_usdt")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True)

def network_selection_keyboard():
    keyboard = [
        [InlineKeyboardButton(text="ARB", callback_data="network_arb")],
        [InlineKeyboardButton(text="TRC", callback_data="network_trc")],
        [InlineKeyboardButton(text="BEP", callback_data="network_bep")],
        [InlineKeyboardButton(text="TON", callback_data="network_ton")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard, resize_keyboard=True)


def check_payment_keyboard():
    keyboard = [
        [InlineKeyboardButton(text="Проверить оплату", callback_data="check_payment")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)



def check_payment():
    keyboard = [
        [InlineKeyboardButton(text="Проверить оплату", callback_data="check_payment")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def channel_link_keyboard(channel_url: str):
    keyboard = [
        [InlineKeyboardButton(text="Перейти в канал", url=channel_url)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
