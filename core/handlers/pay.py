from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


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
        need_name=True,
        need_email=True,
        need_phone_number=True,
        need_shipping_address=True,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=15
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = f'Thank for pay {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.' \
          f'\r\nsome text' \
          f'\r\nsome text 1'
    await message.answer(msg)
