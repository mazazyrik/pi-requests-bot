from typing import List

from aiogram.filters import BaseFilter
from aiogram.types import Message


class CheckChatType(BaseFilter):
    
    def __init__(self, chat_type: List[str]) -> None:
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.chat_type, List):
            if message.chat.type in self.chat_type:
                return True
        return False