from aiogram.dispatcher.filters.state import StatesGroup, State


class AdvertisingREK(StatesGroup):
    PHOTO = State()
    MESSAGE = State()
    CONFIRM = State()
