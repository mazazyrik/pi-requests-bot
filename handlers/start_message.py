import random
from typing import Any

from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart

from filters.filter_check_chat_type import CheckChatType

from data.subloader import get_json
from keyboards import reply

router = Router()


@router.message(CommandStart(), CheckChatType(["private"]))
async def start(message: Message) -> None:
    # await message.bot.send_message(
    #     chat_id=-1002416528732, 
    #     message_thread_id=2, 
    #     text=f"Появился новый <a href='tg://user?id={message.from_user.id}'>пользователь</a>\n\nid: {message.from_user.id}\nusername: @{message.from_user.username}\nfull_name: {message.from_user.full_name}", 
    #     disable_notification = True)
    
    json_message = await get_json("message.json")

    await message.answer(
        text = json_message["welcome_message"],
        reply_markup = reply._keyboard.menu()
    );