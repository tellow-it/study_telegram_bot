from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, InlineKeyboardButton, InlineKeyboardMarkup, \
    ShippingOption, ShippingQuery

keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Оплатить заказ',
            pay=True,
        )
    ],
    [
        InlineKeyboardButton(
            text='Link',
            url='https://nztcoder.com'
        )
    ]
])

BY_SHIPPING = ShippingOption(
    id='by',
    title='Доставка Белпочтой',
    prices=[
        LabeledPrice(
            label='Доставка Белпочтой',
            amount=500,
        )
    ]
)

RU_SHIPPING = ShippingOption(
    id='ru',
    title='Доставка Почтой России',
    prices=[
        LabeledPrice(
            label='Доставка Почтой России',
            amount=200,
        )
    ]
)


async def shipping_check(shipping_query: ShippingQuery, bot: Bot):
    shipping_options = []
    countries = ['BY', 'RU']
    if shipping_query.shipping_address.country_code not in countries:
        return await bot.answer_shipping_query(shipping_query.id, ok=False,
                                               error_message='В вашу страну нету доставки')
    if shipping_query.shipping_address.country_code == 'BY':
        shipping_options.append(BY_SHIPPING)
    elif shipping_query.shipping_address.country_code == 'RU':
        shipping_options.append(RU_SHIPPING)

    await bot.answer_shipping_query(shipping_query.id, ok=True,
                                    shipping_options=shipping_options)


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Покупка',
        description='Study make payments',
        payload='Pay,ent thorugh bot',
        provider_token='381764678:TEST:51179',
        currency='rub',
        prices=[
            LabeledPrice(
                label='доступ к секретной информации))',
                amount=99000
            ),
            LabeledPrice(
                label='ндс',
                amount=20000
            ),
            LabeledPrice(
                label='скидка',
                amount=-20000
            ),
            LabeledPrice(
                label='Бонус',
                amount=-40000
            ),
        ],
        max_tip_amount=5000,
        suggested_tip_amounts=[1000, 2000, 3000, 4000],
        start_parameter='study_tik_bot',
        provider_data=None,
        photo_url='https://i.ibb.co/zGw5X0B/image.jpg',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=False,
        need_email=False,
        need_phone_number=False,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=True,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=keyboards,
        request_timeout=15
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = f'Thank for pay {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.' \
          f'\r\nsome text' \
          f'\r\nsome text 1'
    await message.answer(msg)
