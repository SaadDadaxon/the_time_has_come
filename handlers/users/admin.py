import logging
from datetime import datetime
import asyncio
import random
from aiogram.dispatcher import FSMContext

from keyboards.inline.inline import ulashish, post_callback, confirmation
import requests
from aiogram import types, exceptions
from data.config import ADMINS
from loader import dp, db, bot
from states.group_rek import AdvertisingREK
from states.reklama import Advertising


@dp.message_handler(text='/users_hadis', user_id=ADMINS)
async def user_to_hadis(message: types.Message):
    hadislar = await db.select_all_hadis()
    tasodifiy_hadis = random.choice(hadislar)
    users = await db.select_all_users()
    txt = f"        Kun 📜Hadisi        \n\n"
    txt += f"{tasodifiy_hadis[1]}"
    for user in users:
        await bot.send_message(chat_id=user[3], text=txt, reply_markup=ulashish)


@dp.message_handler(text='/groups_hadis', user_id=ADMINS)
async def user_to_hadis(message: types.Message):
    hadislar = await db.select_all_hadis()
    tasodifiy_hadis = random.choice(hadislar)
    groups = await db.select_all_group()
    txt = f"        Kun 📜Hadisi        \n\n"
    txt += f"{tasodifiy_hadis[1]}"
    for group in groups:
        await bot.send_message(chat_id=group[2], text=txt, reply_markup=ulashish)


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    await message.answer(f"Reklamani Rasmsini yuboring!")
    await Advertising.PHOTO.set()

@dp.message_handler(state=Advertising.PHOTO, user_id=ADMINS, content_types=types.ContentType.ANY)
async def send_ad_to_all(message: types.Message, state: FSMContext):
    try:
        photo = message.photo
        await state.update_data(photo=photo)
        await message.answer(f"Reklamani Textni yuboring!")
        await Advertising.MESSAGE.set()
    except Exception as err:
        print(err)

@dp.message_handler(state=Advertising.MESSAGE, user_id=ADMINS, content_types=types.ContentType.ANY)
async def send_ad_to_all(message: types.Message, state: FSMContext):
    try:
        msg = message.html_text
        await state.update_data(msg=msg)
        await message.answer(f'Reklamani foydalanuvchilarga yuboraymi?', reply_markup=confirmation)
        await Advertising.CONFIRM.set()
    except Exception as err:
        print(err)


@dp.callback_query_handler(post_callback.filter(action='post'), state=Advertising.CONFIRM, user_id=ADMINS)
async def send_ad_to_all(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        photo = data.get("photo")
        msg = data.get("msg")
    await state.finish()
    users = await db.select_all_users()

    unsuccessful_users = []  # Bu ro'yxatga muvaffaqiyatsiz yuborilgan xabarlarni kiritamiz

    for user in users:
        try:
            await bot.send_photo(chat_id=int(user[3]), photo=photo[-1].file_id, caption=msg)
        except (exceptions.BotBlocked, exceptions.UserDeactivated) as e:
            unsuccessful_users.append(user[3])
            await db.delete_user_by_id(user[0])

    if unsuccessful_users:
        # Agar muvaffaqiyatsiz yuborilgan xabarlaringiz bo'lsa, adminlarga yuborish
        await bot.send_message(chat_id=ADMINS[0],
                               text=f"Muvaffaqiyatsiz yuborilgan va bazadan o'chirilgan foydalanuvchilar: {unsuccessful_users}")
    else:
        await bot.send_message(chat_id=ADMINS[0], text=f"Foydalanuvchilarga Reklama yuborildi!")


@dp.message_handler(state=Advertising.CONFIRM, user_id=ADMINS)
async def send_ad_to_all(ms: types.Message):
    await ms.answer(f"Ha Yoki Yoq Tugmasini Bosing!", reply_markup=confirmation)

@dp.callback_query_handler(post_callback.filter(action='cancel'), state=Advertising.CONFIRM, user_id=ADMINS)
async def delete_cancel(call: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()
        await call.answer(f"Reklama O'chirildi")
        await call.message.delete()
    except Exception as a:
        print(a)
        return


@dp.message_handler(text="/admin_commands", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    command = f"/reklama\n"
    command += f"/reklama_gr\n"
    command += f"/user_prayer_time\n"
    command += f"/group_prayer_time\n"
    command += f"/count_user\n"
    command += f"/count_group\n"
    command += f"/users_hadis\n"
    command += f"/groups_hadis\n"
    await message.answer(text=command)


@dp.message_handler(text="/advertising_group", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    txt = str()
    txt += f"Assalom Alaykum Siz Bu bot orqali o'z mahsulotlaringizni reklama qilishingiz mumkin"
    txt += f"Reklama qilish Narxlari https://t.me/@Dadaxon_Saad ga Murojat qilishingiz mumkin!"
    groups = await db.select_all_group()
    for group in groups:
        image = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
        user_id = group[2]
        await bot.send_photo(chat_id=user_id, caption=txt, reply_markup=ulashish, photo=image)


@dp.message_handler(user_id=ADMINS, text="/user_prayer_time")
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        region = user[4]
        msg = str()
        if region is None:
            region = 'Toshkent'
            msg += f"<b>Bu Toshkent vaqti bilan yuborildi!</b>\n\n"
        img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
        today = datetime.today().date()
        data = requests.get(f"https://islomapi.uz/api/present/day?region={region}").json()
        bomdod = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom = data['times']['shom_iftor']
        xufton = data['times']['hufton']
        msg += f'<b>({region} shahri)</b> namoz vaqti {today}\n\n'
        msg += f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
        msg += f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
        msg += f'-------------------------------------\n'
        msg += f'🕢 Bomdod          {bomdod}\n'
        msg += f'-------------------------------------\n'
        msg += f'☀ Quyosh            {quyosh}\n'
        msg += f'-------------------------------------\n'
        msg += f'🕑 Peshin              {peshin}\n'
        msg += f'-------------------------------------\n'
        msg += f'🕓 Asr                    {asr}\n'
        msg += f'-------------------------------------\n'
        msg += f'🕠 Shom                {shom}\n'
        msg += f'-------------------------------------\n'
        msg += f'🕖 Hufton             {xufton}\n'
        msg += f'-------------------------------------\n'
        msg += f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
        msg += f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
        msg += f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
        msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>\n\n'
        msg += f"Agar manzilingizni noto'g'ri belgilagan bo'lsangiz '/foydalanuvchining_manzili' buyrug'gini kiriting"
        await bot.send_photo(chat_id=user[3], photo=img, caption=msg, reply_markup=ulashish, parse_mode='HTML')
        await asyncio.sleep(0.05)


@dp.message_handler(user_id=ADMINS, text="/group_prayer_time")
async def send_ad_to_all(message: types.Message):
    groups = await db.select_all_group()
    for group in groups:
        img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
        today = datetime.today().date()
        data = requests.get(f"https://islomapi.uz/api/present/day?region={group[3]}").json()
        bomdod = data['times']['tong_saharlik']
        quyosh = data['times']['quyosh']
        peshin = data['times']['peshin']
        asr = data['times']['asr']
        shom = data['times']['shom_iftor']
        xufton = data['times']['hufton']
        msg = f'<b>({group[3]} shahri)</b> namoz vaqti {today}\n\n'
        msg += f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
        msg += f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
        msg += f'-------------------------------------\n'
        msg += f'🕢 Bomdod          {bomdod}\n'
        msg += f'-------------------------------------\n'
        msg += f'☀ Quyosh            {quyosh}\n'
        msg += f'-------------------------------------\n'
        msg += f'🕑 Peshin              {peshin}\n'
        msg += f'-------------------------------------\n'
        msg += f'🕓 Asr                    {asr}\n'
        msg += f'-------------------------------------\n'
        msg += f'🕠 Shom                {shom}\n'
        msg += f'-------------------------------------\n'
        msg += f'🕖 Hufton             {xufton}\n'
        msg += f'-------------------------------------\n'
        msg += f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
        msg += f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
        msg += f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
        msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>\n\n'
        msg += f"Guruhning manzilingizni noto'g'ri belgilagan bo'lsangiz '/guruh_manzili' buyrug'gini kiriting"
        await bot.send_photo(chat_id=group[2], photo=img, caption=msg, reply_markup=ulashish, parse_mode='HTML')
    await asyncio.sleep(0.05)


@dp.message_handler(user_id=ADMINS, text="/count_user")
async def count_user(ms: types.Message):
    count = await db.count_users()
    await ms.answer(f"Botda {count}ta 🧔foydalanuvchisi bor")

    user_info = await db.select_all_users()
    for info in user_info:
        await ms.answer(f"Foydalanuvchining full_name: {info[1]}\n"
                        f"foydalanuvchining username: @{info[2]}")


@dp.message_handler(user_id=ADMINS, text="/count_group")
async def count_user(ms: types.Message):
    count = await db.count_group()
    await ms.answer(f"Botda {count}ta 👥guruh bor")

    group_info = await db.select_all_group()
    for info in group_info:
        await ms.answer(f"Guruhning full_name: {info[1]}\n")


@dp.message_handler(text="/reklamagroup", user_id=ADMINS[0])
async def send_ad_to_all(message: types.Message):
    await message.answer(f"Reklamani Rasmsini yuboring!")
    await AdvertisingREK.PHOTO.set()


@dp.message_handler(state=AdvertisingREK.PHOTO, user_id=ADMINS[0], content_types=types.ContentType.ANY)
async def send_ad_to_all(message: types.Message, state: FSMContext):
    try:
        photo = message.photo
        await state.update_data(photo=photo)
        await message.answer(f"Reklamani Textni yuboring!")
        await AdvertisingREK.MESSAGE.set()
    except Exception as err:
        print(err)


@dp.message_handler(state=AdvertisingREK.MESSAGE, user_id=ADMINS[0], content_types=types.ContentType.ANY)
async def send_ad_to_all(message: types.Message, state: FSMContext):
    try:
        msg = message.html_text
        await state.update_data(msg=msg)
        await message.answer(f'Reklamani foydalanuvchilarga yuboraymi?', reply_markup=confirmation)
        await AdvertisingREK.CONFIRM.set()
    except Exception as err:
        print(err)


@dp.callback_query_handler(post_callback.filter(action='post'), state=AdvertisingREK.CONFIRM, user_id=ADMINS[0])
async def send_ad_to_all(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        photo = data.get("photo")
        msg = data.get("msg")
    await state.finish()
    groups = await db.select_all_group()

    unsuccessful_users = []  # Bu ro'yxatga muvaffaqiyatsiz yuborilgan xabarlarni kiritamiz

    for group in groups:
        try:
            await bot.send_photo(chat_id=int(group[2]), photo=photo[-1].file_id, caption=msg)
        except (exceptions.BotBlocked, exceptions.UserDeactivated) as e:
            unsuccessful_users.append(group[1])
            await db.delete_group(group[0])

    if unsuccessful_users:
        # Agar muvaffaqiyatsiz yuborilgan xabarlaringiz bo'lsa, adminlarga yuborish
        await bot.send_message(chat_id=ADMINS[0],
                               text=f"Muvaffaqiyatsiz yuborilgan va bazadan o'chirilgan gruhlar: {unsuccessful_users}")
    else:
        await bot.send_message(chat_id=ADMINS[0], text=f"Gruhlarga Reklama yuborildi!")


@dp.message_handler(state=AdvertisingREK.CONFIRM, user_id=ADMINS[0])
async def send_ad_to_all(ms: types.Message):
    await ms.answer(f"Ha Yoki Yoq Tugmasini Bosing!", reply_markup=confirmation)


@dp.callback_query_handler(post_callback.filter(action='cancel'), state=AdvertisingREK.CONFIRM, user_id=ADMINS[0])
async def delete_cancel(call: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()
        await call.answer(f"Reklama O'chirildi")
        await call.message.delete()
    except Exception as a:
        print(a)
        return
