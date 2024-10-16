from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from keyboards import inline


class CheckSubscription(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        chat_member = await event.bot.get_chat_member("@trichetyrnadcat", event.from_user.id)

        if chat_member.status == "left":
            await event.answer(
                "Подпишись на канал @trichetyrnadcat, чтобы пользоваться ботом!",
                reply_markup=inline._keyboard.sub_channel
            )
        else:
            return await handler(event, data)