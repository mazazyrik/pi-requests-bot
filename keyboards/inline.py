from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class _keyboard:
    sub_channel = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Подписаться", url="https://t.me/trichetyrnadcat")
            ]
        ]
    )

    sub_bot = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Прислать новость", url="https://t.me/OpiEditBot")
            ]
        ]
    )