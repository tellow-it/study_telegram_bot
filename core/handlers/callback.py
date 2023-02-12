from aiogram import Bot
from aiogram.types import CallbackQuery
from core.utils.callback import MacInfo

# async def select_macbook(call: CallbackQuery):
#     brend = call.data.split()[0]
#     model = call.data.split('_')[1]
#     size = call.data.split('_')[2]
#     year = call.data.split('_')[3]
#
#     answer = f'{call.message.from_user.first_name}, u chose {brend}---{model}' \
#              f'---{size}----{year}'
#     await call.message.answer(answer)
#     await call.answer()


async def select_macbook(call: CallbackQuery, callback_data: MacInfo):
    brend = callback_data.brend
    model = callback_data.model
    size = callback_data.size
    year = callback_data.year

    answer = f'{call.message.from_user.first_name}, u chose {brend}---{model}' \
             f'---{size}----{year}'
    await call.message.answer(answer)
    await call.answer()