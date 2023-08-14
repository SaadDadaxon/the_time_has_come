from aiogram.dispatcher.filters.state import StatesGroup, State


class Advertising(StatesGroup):
    PHOTO = State()
    MESSAGE = State()
    CONFIRM = State()

