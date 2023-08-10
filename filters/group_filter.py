from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsGroup(BoundFilter):
    async def check(self, ms: types.Message) -> bool:
        return ms.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )


class IsGroupCall(BoundFilter):
    async def check(self, ms: types.CallbackQuery) -> bool:
        return ms.message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )
