from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from filters.group_filter import IsGroup
from filters.private_filter import IsPrivates
from loader import dp


@dp.message_handler(IsGroup(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/guruh_manzili - Guruhning manzilini o'zgartirish")
    
    await message.answer("\n".join(text))


@dp.message_handler(IsPrivates(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/faydalanuvchining_manzili - Foydalanuvchining manzilini o'zgartirish")

    await message.answer("\n".join(text))
