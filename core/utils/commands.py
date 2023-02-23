from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Start work'
        ),
        BotCommand(
            command='help',
            description='Help'
        ),
        BotCommand(
            command='cancel',
            description='Cancel'
        ),
        BotCommand(
            command='inline',
            description='Inline keyboard'
        ),
        BotCommand(
            command='pay',
            description='pay'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
