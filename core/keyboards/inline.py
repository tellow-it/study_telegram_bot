from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callback import MacInfo

select_macbook = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='macbook 13 pro 2020',
                callback_data='apple_pro_13_2020'
            )
        ],
        [
            InlineKeyboardButton(
                text='macbook 14 pro 2021',
                callback_data='apple_pro_14_2021'
            )
        ],
        [
            InlineKeyboardButton(
                text='macbook 16 pro 2019',
                callback_data='apple_pro_13_2019'
            )
        ],
        [
            InlineKeyboardButton(
                text='Link1',
                url='https://github.com/tellow-it/study_telegram_bot'
            )
        ],
        [
            InlineKeyboardButton(
                text='Profile',
                url='https://t.me/TeLLoW'
            )
        ],
    ]
)


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='macbook 13 pro 2020',
                            callback_data=MacInfo(brend='apple', model='pro', size='13', year='2020'))
    keyboard_builder.button(text='macbook 14 pro 2021',
                            callback_data=MacInfo(brend='apple', model='pro', size='14', year='2021'))
    keyboard_builder.button(text='air macbook 16 pro 2019',
                            callback_data=MacInfo(brend='apple', model='pro', size='16', year='2019'))
    keyboard_builder.button(text='Link1',
                            url='https://github.com/tellow-it/study_telegram_bot')
    keyboard_builder.button(text='Profile',
                            url='https://t.me/TeLLoW')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
