from aiogram.filters.callback_data import CallbackData


class MacInfo(CallbackData, prefix='mac'):
    brend: str
    model: str
    size: str
    year: str
