from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsPrivate(BoundFilter):
    async def check(self, ms: types.CallbackQuery) -> bool:
        return ms.message.chat.type == types.ChatType.PRIVATE


class IsPrivates(BoundFilter):
    async def check(self, ms: types.Message) -> bool:
        return ms.chat.type == types.ChatType.PRIVATE
