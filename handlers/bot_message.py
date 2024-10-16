import random
from typing import Any

from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart

from filters.filter_check_chat_type import CheckChatType

from data.subloader import get_json
from keyboards import reply as kr

router = Router()


@router.message(CheckChatType(["private"]))
async def start(message: Message) -> None:
    json_message = await get_json("message.json")

    if message.text.lower() == "как предложить пост?🧐":
        await message.answer(text = json_message["request_message"])

    
    else:
        await message.reply("Я передал твое сообщение😉")
        await message.forward(
            chat_id=-1002406911260,
            message_thread_id=1633,
            disable_notification=True,
            protect_content=False
        )