import asyncio
import logging

import asyncpg
from aiogram import Bot, Dispatcher
from aiogram import types

from core.filtres.iscontact import IsTrueContact
from core.handlers.callback import select_macbook
from core.handlers.contact import get_true_contact, get_fake_contact
from core.handlers.pay import order, pre_checkout_query, successful_payment, shipping_check
from core.settings import settings
from core.handlers.basic import get_start, get_photo, get_hello, get_location, get_inline
from aiogram.filters import Command, CommandStart
from aiogram import F

from core.middlewares.dbmiddlewares import DbSession

from core.utils.callback import MacInfo
from core.utils.commands import set_commands

token = settings.bots.bot_token
admin_id = settings.bots.admin_id


async def create_pool():
    return await asyncpg.create_pool(user='postgres', password='DtnthDgjkt2002', database='postgres',
                                     host='localhost', port=5432, command_timeout=60, )


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
    pool_connect = await create_pool()
    dp = Dispatcher()
    dp.update.middleware.register(DbSession(pool_connect))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(order, Command(commands=['pay']))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, F.content_type.in_({'successful_payment'}))
    dp.shipping_query.register(shipping_check)
    dp.message.register(get_inline, Command(commands=['inline']))
    dp.callback_query.register(select_macbook, MacInfo.filter(F.model == 'pro'))
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
