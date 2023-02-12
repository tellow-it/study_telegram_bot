import json

from aiogram import Bot
from aiogram.types import Message

from core.keyboards.inline import select_macbook, get_inline_keyboard
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard


async def get_inline(message: Message, bot: Bot):
    await message.answer(f'Привет {message.from_user.first_name}. Инлайн кнопки', reply_markup=get_inline_keyboard())


async def get_start(message: Message, bot: Bot):
    await message.answer(f'Привет {message.from_user.first_name}. Добро пожаловать!',
                         reply_markup=get_reply_keyboard())


async def get_location(message: Message, bot: Bot):
    await message.answer(f'Ты отправил локацию'
                         f'{message.location.latitude}\n'
                         f'{message.location.longitude}',
                         reply_markup=loc_tel_poll_keyboard)


async def get_photo(message: Message, bot: Bot):
    await message.answer('Отлично, ты отправил фото, сохраня ее...')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, f'{message.photo[-1].file_id}.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе привет!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
