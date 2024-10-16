from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, ReplyKeyboardRemove

class _keyboard:
    def menu() -> ReplyKeyboardMarkup:
        keyboard = []

        keyboard.append([KeyboardButton(text="Как предложить пост?🧐")])

        kb = ReplyKeyboardMarkup(
            keyboard=keyboard,
            resize_keyboard=True,
            one_time_keyboard=False,
            input_field_placeholder="Ты сегодня прекрасно выглядишь",
            selective=True
        )
        return kb