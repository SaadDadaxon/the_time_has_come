import asyncpg
import requests
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.inline import joy, viloyat_menu
from keyboards.default import reply
from loader import dp, db, bot
from data.config import ADMINS
from filters.private_filter import IsPrivates


@dp.message_handler(CommandStart(), IsPrivates())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer("Xush kelibsiz!")

    # ADMINGA xabar beramiz
    count = await db.count_users()
    msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor.\n"
    msg += f"Foydalanuvchi id:{user[3]}\n"
    msg += f"Foydalanuvchini profili @{message.from_user.username}\n"
    msg += f"Admin buyruqlari /admin_commands"
    await bot.send_message(chat_id=ADMINS[0], text=msg)

    txt = f"<b>Assalomu Alaykum va Raxmatullohu va Barakatuh Mr.{message.from_user.full_name}! siz bu Botdan Nomoz vaqtlarini bilib olishingiz mumkin mumkin</b>"
    img = open("image/8e7f59399b819d8cd081b529c20c894b.jpg", "rb")
    await message.answer_photo(img, caption=txt, reply_markup=reply.bosh_menu, parse_mode="html")
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


@dp.message_handler(text='🕰Nomoz Vaqtlari')
async def nomoz_button(ms: types.Message):
    await ms.answer(text='Tanlang!', reply_markup=joy)


# city = "nukus"
# url = f"https://islomapi.uz/api/present/day?region={city}"
#
#
# r = requests.get(url)
# res = r.json()
# print(res)
# print(res['times']['tong_saharlik'])

