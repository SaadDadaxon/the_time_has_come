from aiogram import types
from loader import dp, bot
from keyboards.default.reply import info_menu, bosh_menu


@dp.message_handler(text="⚙Bot Haqida")
async def bot_info(ms: types.Message):
    await ms.answer(text='Bot Haqida', reply_markup=info_menu)


@dp.message_handler(text="📝Bot Ma'lumoti")
async def bot_info(ms: types.Message):
    text = f"Bot Mo'minlarga foyda qilish maqsadida yaratildi\n"
    text += f"Nomoz vaqtlarini🕰\n"
    text += f"Hadislarni📜 yuboradigan va\n"
    text += f"Hadislarni📜 botning Kutubxonasiga kiritadigan buyruqlarni bor\n"
    text += f"Bot Sizga foydasi tekanidan hursandmiz\n"
    await ms.answer(text)


@dp.message_handler(text="🧔Bot Yaratuvchisi💻")
async def bot_info(ms: types.Message):
    await ms.answer(f"https://t.me/Dadaxon_Saad")


@dp.message_handler(text="⏪Ortga")
async def bot_info(ms: types.Message):
    await ms.answer(text='Bosh Sahifa', reply_markup=bosh_menu)

