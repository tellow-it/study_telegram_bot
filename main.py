import asyncio
import logging
from aiogram import Bot, Dispatcher
from core.settings import settings
from core.handlers.basic import get_start

token = settings.bots.bot_token
admin_id = settings.bots.admin_id


async def start_bot(bot: Bot):
    await bot.send_message(admin_id, 'Bot start')


async def stop_bot(bot: Bot):
    await bot.send_message(admin_id, 'Bot stopped')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s"
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
