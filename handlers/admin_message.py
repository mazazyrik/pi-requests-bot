import random
from typing import Any

from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart

from filters.filter_check_chat_type import CheckChatType
from filters.is_admin import IsAdmin

from data.subloader import get_json

from keyboards import inline

router = Router()


@router.message(F.text.lower() == "1", CheckChatType(["private"]), IsAdmin([673638087, 387435447]))
async def start(message: Message) -> None:
    json_message = await get_json("message.json")

    await message.answer(
        text = json_message["sub_bot"],
        reply_markup=inline._keyboard.sub_bot
    );
