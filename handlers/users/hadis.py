from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.inline import confirmation, post_callback
from loader import bot, db, dp
from data.config import ADMINS
from filters.private_filter import IsPrivates, IsPrivate
from states.hadis_add import HadisAdd
from aiogram.dispatcher.filters import Command
import random


@dp.message_handler(text="📜Hadis")
async def hadis_to_see(ms: types.Message):
    hadislar = await db.select_all_hadis()
    tasodifiy_hadis = random.choice(hadislar)
    await ms.answer(tasodifiy_hadis[1])


@dp.message_handler(text="📜Hadis qo'shish➕")
async def hadis_add(ms: types.Message):
    await ms.answer('Iltimos Hadisni kiritishdan oldin Sahih ekanligiga ishonch hosli qiling!\n')
    await ms.answer(f"Namuna:\n")
    await ms.answer(f"Amr ibn Oss roziyallohu anhumodan rivoyat qilinadi: «Rasululloh sollallohu alayhi vasallam:\n"
                    f"«Bizning ro‘zamiz ila ahli kitoblarning ro‘zasi orasidagi farq saharlik yeyishidadir», dedilar».\n"
                    f"\n"
                    f"Buxoriy rivoyat qilganlar.\n")
    await ms.answer("/hadis buyrug'ini kiriting")


@dp.message_handler(Command('hadis'))
async def create_post(ms: types.Message):
    await ms.answer("Hadisni Kutubxonamizga kiritishni boshlang...")
    await HadisAdd.Text.set()


@dp.message_handler(IsPrivates(), state=HadisAdd.Text)
async def text_add(ms: types.Message, state: FSMContext):
    await state.update_data(text=ms.text, mention=ms.from_user.get_mention())
    await ms.answer(f"Hadisni tekshiruvga yuboraymi?", reply_markup=confirmation)
    await HadisAdd.next()


@dp.callback_query_handler(IsPrivate(), post_callback.filter(action="post"), state=HadisAdd.Confirm)
async def finish(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get('text')
        mention = data.get('mention')
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer('Hadis tekshiruvga yuborildi...')
    await bot.send_message(ADMINS[0], f"Foydalanuvchi {mention} quydagi Hadisni Hadislar kutibxonasiga kiritmoqchi: ")
    await bot.send_message(ADMINS[0], text, parse_mode='HTML', reply_markup=confirmation)


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=HadisAdd.Confirm)
async def cancel_post(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer('Hadisda Xatolik Bor!')


@dp.message_handler(state=HadisAdd.Confirm)
async def approve_post(ms: types.Message):
    await ms.answer('Chop etish yoki rad etish tugmasini bosing!', reply_markup=confirmation)


@dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS)
async def cancel_post(call: types.CallbackQuery):
    await call.answer(f"Chop etishga ruxsat etdingiz", show_alert=True)
    text = call.message.text
    await db.add_hadis(hadis_text=text)
    await call.message.answer('Hadis Kutubxonaga kiritildi✅')
    await call.message.delete_reply_markup()


@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS)
async def cancel_post(call: types.CallbackQuery):
    await call.answer(f"Hadis xato yozilibdi!", show_alert=True)
    await call.message.edit_reply_markup()


