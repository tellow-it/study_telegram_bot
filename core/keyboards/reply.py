from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Button 1 row 1'),
            KeyboardButton(text='Button 2 row 1'),
            KeyboardButton(text='Button 3 row 1')
        ],
        [
            KeyboardButton(text='Button 1 row 2'),
            KeyboardButton(text='Button 2 row 2'),
            KeyboardButton(text='Button 3 row 2'),
            KeyboardButton(text='Button 4 row 2')
        ],
        [
            KeyboardButton(text='Button 1 row 3'),
            KeyboardButton(text='Button 2 row 3'),
            KeyboardButton(text='Button 3 row 3'),
            KeyboardButton(text='Button 4 row 3')
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери кнопку'
)

loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Telephone', request_contact=True)],
    [KeyboardButton(text='Location', request_location=True)],
    [KeyboardButton(text='Create quiz', request_poll=KeyboardButtonPollType())]
],
    resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='Выбери кнопку'
)


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Кнопка 1')
    keyboard_builder.button(text='Кнопка 2')
    keyboard_builder.button(text='Кнопка 3')
    keyboard_builder.button(text='Отправить геолокацию', request_location=True)
    keyboard_builder.button(text='Отправить телефон', request_contact=True)
    keyboard_builder.button(text='Create quiz', request_poll=KeyboardButtonPollType())
    keyboard_builder.adjust(3, 1, 2)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=False,
                                      input_field_placeholder='Выбери кнопку')
