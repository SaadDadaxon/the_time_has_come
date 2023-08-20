import asyncpg
from aiogram.dispatcher import FSMContext
from aiogram.utils import exceptions

from filters.group_filter import IsGroup
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS
from keyboards.inline.inline import viloyat_menu, post_callback, confirmation
from states.group_rek import AdvertisingREK


@dp.message_handler(CommandStart(), IsGroup())
async def bot_start(message: types.Message):
    try:
        group = await db.add_group(group_id=message.chat.id, group_name=message.chat.title)
    except asyncpg.exceptions.UniqueViolationError:
        group = await db.select_group(group_id=message.chat.id)

    await message.answer("Assalomu Alaykum va Rahmatullohu va Barakathu\n"
                         "Bot Faollashdi")

    # ADMINGA xabar beramiz
    count = await db.count_group()
    msg = f"{group[1]} bazaga qo'shildi.\nBazada {count} ta guruh bor.\n"
    msg += f"Gruhning nomi {group[1]}\n"
    await bot.send_message(chat_id=ADMINS[0], text=msg)

    txt = f"<b>Assalomu Alaykum va Raxmatullohu va Barakatuh {group[1]}! ahli siz bu bot guruhga har kunlik nomoz vaqlarini yuborib turadi</b>"
    img = open("image/8e7f59399b819d8cd081b529c20c894b.jpg", "rb")
    await message.answer_photo(img, caption=txt, parse_mode="html", reply_markup=viloyat_menu)
