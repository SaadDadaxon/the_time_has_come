from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    async def check(self, ms: types.Message) -> bool:
        member = await ms.chat.get_member(ms.from_user.id)
        return member.is_chat_member()



