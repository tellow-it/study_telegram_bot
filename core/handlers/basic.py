import json

from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}. Добро пожаловать!')
    await message.answer(f'Привет {message.from_user.first_name}. Добро пожаловать!')
    await message.reply(f'Привет {message.from_user.first_name}. Добро пожаловать!')


async def get_photo(message: Message, bot: Bot):
    await message.answer('Отлично, ты отправил фото, сохраня ее...')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, f'{message.photo[-1].file_id}.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе привет!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)