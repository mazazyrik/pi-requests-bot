import asyncio
import logging

from aiogram import Bot, Dispatcher

from routers import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


bot = Bot(token="7452638953:AAE_pQRLxNXBfYqY8SDGq2TeysXE_xTkgCE")


async def main():
    dp = Dispatcher()
    dp.include_routers(requests.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=False)


if __name__ == "__main__":
    asyncio.run(main())
