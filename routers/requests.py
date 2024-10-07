from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext

from utils.help_text import welcome_message, request_text
from utils.states import Request


CHANNEL_URL = 'https://t.me/trichetyrnadcat'
router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(
            text='Предложить пост',
            callback_data='request'
        ),
        InlineKeyboardButton(
            text='Перейти в канал',
            url=CHANNEL_URL
        ),
        # InlineKeyboardButton(
        #     text='Связаться с админом',
        #     callback_data='contact'
        # ) оставляем на потом по надобности
    )

    await message.answer(
        text=welcome_message,
        reply_markup=keyboard.adjust(1).as_markup()
    )


@router.callback_query(F.data == 'request')
async def cmd_request(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Request.message)
    await callback.message.answer(
        text=request_text
    )


@router.message(Request.message)
async def send_request(message: Message, state: FSMContext):
    await message.forward(
        chat_id=-1002406911260,
        message_thread_id=1633,
        disable_notification=True,
        protect_content=False
    )

    await state.clear()

    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(
            text='Предложить еще один пост',
            callback_data='request'
        ),
    )
    await message.answer(
        text='Ваша заявка успешно отправлена!',
        reply_markup=keyboard.adjust(1).as_markup()
    )
