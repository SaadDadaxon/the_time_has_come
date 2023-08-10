from aiogram.dispatcher.filters.state import State, StatesGroup


class HadisAdd(StatesGroup):
    Text = State()
    Confirm = State()
