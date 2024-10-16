import asyncio
from aiogram import Bot, Dispatcher

import handlers

import handlers.admin_message
import handlers.bot_message
from middlewares.check_sub import CheckSubscription
from middlewares.antiflood import AntiFloodMiddleware

from config_reader import config

import urllib3

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def main() -> None:
    bot = Bot(config.bot_token.get_secret_value())
    dp = Dispatcher()
    

    # dp.message.middleware(AntiFloodMiddleware(0.2))
    dp.message.middleware(CheckSubscription())


    dp.include_routers(
        handlers.start_message.router,
        handlers.admin_message.router,
        handlers.bot_message.router
    )

    await bot.delete_webhook(drop_pending_updates=False)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())