import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram import types

from core.filtres.iscontact import IsTrueContact
from core.handlers.contact import get_true_contact, get_fake_contact
from core.settings import settings
from core.handlers.basic import get_start, get_photo, get_hello, get_location
from aiogram.filters import Command, CommandStart
from aiogram import F

from core.utils.commands import set_commands

token = settings.bots.bot_token
admin_id = settings.bots.admin_id


async def start_bot(bot: Bot):
    await set_commands(bot)
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
    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_photo, F.content_type.in_({'photo'}))
    dp.message.register(get_hello, F.text == 'Привет')
    dp.message.register(get_location, F.location)
    dp.message.register(get_true_contact, IsTrueContact())
    dp.message.register(get_fake_contact)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
