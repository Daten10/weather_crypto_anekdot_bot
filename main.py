import asyncio
import logging
from config import dp, bot, set_my_menu

from handlers import handler_router


async def main():
    await set_my_menu()
    dp.include_router(handler_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
