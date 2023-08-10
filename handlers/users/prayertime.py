import time
import types
from aiogram.dispatcher.filters import Command
from filters.private_filter import IsPrivate
import requests
from aiogram.types import Message, CallbackQuery
from loader import dp, bot, db
from keyboards.inline.inline import viloyat_menu, ulashish, uzgargan_menu
import datetime
from datetime import *


"""
city = "nukus"

url = f"https://islomapi.uz/api/present/day?region={Toshkent}"

r = requests.get(url)
print(r.status_code)
res = r.json()
print(res)
"""


@dp.callback_query_handler(text_contains="uzbek")
async def vaqt(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    await call.message.answer_photo(img, reply_markup=viloyat_menu)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='Toshkent')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    data = requests.get("https://islomapi.uz/api/present/day?region=Toshkent").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    msg = f'<b>(Toshkent shahri)</b> namoz vaqti {today}\n\n'
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
    await bot.send_photo(chat_id=call.from_user.id, photo=img, caption=msg, reply_markup=ulashish, parse_mode='HTML')
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='Andijon')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    data = requests.get("https://islomapi.uz/api/present/day?region=Andijon").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    await call.message.answer_photo(img, f'<b>(Andijon shahri)</b> namoz vaqti {today}\n\n'
                                         f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                         f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                         f'-------------------------------------\n'
                                         f'🕢 Bomdod          {bomdod}\n'
                                         f'-------------------------------------\n'
                                         f'☀ Quyosh            {quyosh}\n'
                                         f'-------------------------------------\n'
                                         f'🕑 Peshin              {peshin}\n'
                                         f'-------------------------------------\n'
                                         f'🕓 Asr                    {asr}\n'
                                         f'-------------------------------------\n'
                                         f'🕠 Shom                {shom}\n'
                                         f'-------------------------------------\n'
                                         f'🕖 Hufton             {xufton}\n'
                                         f'-------------------------------------\n'
                                         f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                         f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                         f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                         f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', reply_markup=ulashish, parse_mode='HTML')
    us_id = await db.select_user(telegram_id=call.message.chat.id)
    await db.update_user_region(user_region='Andijon', telegram_id=us_id[3])
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='Buxoro')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    data = requests.get("https://islomapi.uz/api/present/day?region=Buxoro").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    await call.message.answer_photo(img, f'<b>(Buxoro shahri)</b> namoz vaqti {today}\n\n'
                                         f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                         f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                         f'-------------------------------------\n'
                                         f'🕢 Bomdod          {bomdod}\n'
                                         f'-------------------------------------\n'
                                         f'☀ Quyosh            {quyosh}\n'
                                         f'-------------------------------------\n'
                                         f'🕑 Peshin              {peshin}\n'
                                         f'-------------------------------------\n'
                                         f'🕓 Asr                    {asr}\n'
                                         f'-------------------------------------\n'
                                         f'🕠 Shom                {shom}\n'
                                         f'-------------------------------------\n'
                                         f'🕖 Hufton             {xufton}\n'
                                         f'-------------------------------------\n'
                                         f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                         f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                         f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                         f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', reply_markup=ulashish, parse_mode='HTML')
    us_id = await db.select_user(telegram_id=call.message.chat.id)
    await db.update_user_region(user_region='Buxoro', telegram_id=us_id[3])
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains="Farg'ona")
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    data = requests.get("https://islomapi.uz/api/present/day?region=Farg'ona").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    await call.message.answer_photo(img, f"<b>(Farg'ona shahri)</b> namoz vaqti {today}\n\n"
                                         f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                         f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                         f'-------------------------------------\n'
                                         f'🕢 Bomdod          {bomdod}\n'
                                         f'-------------------------------------\n'
                                         f'☀ Quyosh            {quyosh}\n'
                                         f'-------------------------------------\n'
                                         f'🕑 Peshin              {peshin}\n'
                                         f'-------------------------------------\n'
                                         f'🕓 Asr                    {asr}\n'
                                         f'-------------------------------------\n'
                                         f'🕠 Shom                {shom}\n'
                                         f'-------------------------------------\n'
                                         f'🕖 Hufton             {xufton}\n'
                                         f'-------------------------------------\n'
                                         f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                         f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                         f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                         f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', reply_markup=ulashish, parse_mode='HTML')
    us_id = await db.select_user(telegram_id=call.message.chat.id)
    await db.update_user_region(user_region="Farg'ona", telegram_id=us_id[3])
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='Jizzax')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    data = requests.get("https://islomapi.uz/api/present/day?region=Jizzax").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    await call.message.answer_photo(img, f'<b>(Jizzax shahri)</b> namoz vaqti {today}\n\n'
                                         f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                         f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                         f'-------------------------------------\n'
                                         f'🕢 Bomdod          {bomdod}\n'
                                         f'-------------------------------------\n'
                                         f'☀ Quyosh            {quyosh}\n'
                                         f'-------------------------------------\n'
                                         f'🕑 Peshin              {peshin}\n'
                                         f'-------------------------------------\n'
                                         f'🕓 Asr                    {asr}\n'
                                         f'-------------------------------------\n'
                                         f'🕠 Shom                {shom}\n'
                                         f'-------------------------------------\n'
                                         f'🕖 Hufton             {xufton}\n'
                                         f'-------------------------------------\n'
                                         f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                         f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                         f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                         f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', reply_markup=ulashish, parse_mode='HTML')
    us_id = await db.select_user(telegram_id=call.message.chat.id)
    await db.update_user_region(user_region='Jizzax', telegram_id=us_id[3])
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='Xorazm')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    data = requests.get("https://islomapi.uz/api/present/day?region=Xorazm").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    await call.message.answer_photo(img, f'<b>(Xorazm shahri)</b> namoz vaqti {today}\n\n'
                                         f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                         f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                         f'-------------------------------------\n'
                                         f'🕢 Bomdod          {bomdod}\n'
                                         f'-------------------------------------\n'
                                         f'☀ Quyosh            {quyosh}\n'
                                         f'-------------------------------------\n'
                                         f'🕑 Peshin              {peshin}\n'
                                         f'-------------------------------------\n'
                                         f'🕓 Asr                    {asr}\n'
                                         f'-------------------------------------\n'
                                         f'🕠 Shom                {shom}\n'
                                         f'-------------------------------------\n'
                                         f'🕖 Hufton             {xufton}\n'
                                         f'-------------------------------------\n'
                                         f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                         f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                         f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                         f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', reply_markup=ulashish, parse_mode='HTML')
    us_id = await db.select_user(telegram_id=call.message.chat.id)
    await db.update_user_region(user_region='Xorazm', telegram_id=us_id[3])
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='Namangan')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    data = requests.get("https://islomapi.uz/api/present/day?region=Namangan").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    await call.message.answer_photo(img, f'<b>(Namangan shahri)</b> namoz vaqti {today}\n\n'
                                         f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                         f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                         f'-------------------------------------\n'
                                         f'🕢 Bomdod          {bomdod}\n'
                                         f'-------------------------------------\n'
                                         f'☀ Quyosh            {quyosh}\n'
                                         f'-------------------------------------\n'
                                         f'🕑 Peshin              {peshin}\n'
                                         f'-------------------------------------\n'
                                         f'🕓 Asr                    {asr}\n'
                                         f'-------------------------------------\n'
                                         f'🕠 Shom                {shom}\n'
                                         f'-------------------------------------\n'
                                         f'🕖 Hufton             {xufton}\n'
                                         f'-------------------------------------\n'
                                         f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                         f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                         f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                         f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', reply_markup=ulashish, parse_mode='HTML')
    us_id = await db.select_user(telegram_id=call.message.chat.id)
    await db.update_user_region(user_region='Namangan', telegram_id=us_id[3])
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='Navoi')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    data = requests.get("https://islomapi.uz/api/present/day?region=Navoi").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    await call.message.answer_photo(img, f'<b>(Navoi shahri)</b> namoz vaqti {today}\n\n'
                                         f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                         f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                         f'-------------------------------------\n'
                                         f'🕢 Bomdod          {bomdod}\n'
                                         f'-------------------------------------\n'
                                         f'☀ Quyosh            {quyosh}\n'
                                         f'-------------------------------------\n'
                                         f'🕑 Peshin              {peshin}\n'
                                         f'-------------------------------------\n'
                                         f'🕓 Asr                    {asr}\n'
                                         f'-------------------------------------\n'
                                         f'🕠 Shom                {shom}\n'
                                         f'-------------------------------------\n'
                                         f'🕖 Hufton             {xufton}\n'
                                         f'-------------------------------------\n'
                                         f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                         f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                         f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                         f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', reply_markup=ulashish, parse_mode='HTML')
    us_id = await db.select_user(telegram_id=call.message.chat.id)
    await db.update_user_region(user_region='Navoi', telegram_id=us_id[3])
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='Qashqadaryo')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    data = requests.get("https://islomapi.uz/api/present/day?region=Qarshi").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    await call.message.answer_photo(img, f'<b>(Qashqadaryo shahri)</b> namoz vaqti {today}\n\n'
                                         f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                         f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                         f'-------------------------------------\n'
                                         f'🕢 Bomdod          {bomdod}\n'
                                         f'-------------------------------------\n'
                                         f'☀ Quyosh            {quyosh}\n'
                                         f'-------------------------------------\n'
                                         f'🕑 Peshin              {peshin}\n'
                                         f'-------------------------------------\n'
                                         f'🕓 Asr                    {asr}\n'
                                         f'-------------------------------------\n'
                                         f'🕠 Shom                {shom}\n'
                                         f'-------------------------------------\n'
                                         f'🕖 Hufton             {xufton}\n'
                                         f'-------------------------------------\n'
                                         f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                         f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                         f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                         f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', reply_markup=ulashish, parse_mode='HTML')
    us_id = await db.select_user(telegram_id=call.message.chat.id)
    await db.update_user_region(user_region='Qarshi', telegram_id=us_id[3])
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='Qoraqalpog')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    data = requests.get("https://islomapi.uz/api/present/day?region=Nukus").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    await call.message.answer_photo(img, f'<b>(Nukus shahri)</b> namoz vaqti {today}\n\n'
                                         f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                         f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                         f'-------------------------------------\n'
                                         f'🕢 Bomdod          {bomdod}\n'
                                         f'-------------------------------------\n'
                                         f'☀ Quyosh            {quyosh}\n'
                                         f'-------------------------------------\n'
                                         f'🕑 Peshin              {peshin}\n'
                                         f'-------------------------------------\n'
                                         f'🕓 Asr                    {asr}\n'
                                         f'-------------------------------------\n'
                                         f'🕠 Shom                {shom}\n'
                                         f'-------------------------------------\n'
                                         f'🕖 Hufton             {xufton}\n'
                                         f'-------------------------------------\n'
                                         f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                         f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                         f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                         f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', reply_markup=ulashish, parse_mode='HTML')
    us_id = await db.select_user(telegram_id=call.message.chat.id)
    await db.update_user_region(user_region='Nukus', telegram_id=us_id[3])
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='Samarqand')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    data = requests.get("https://islomapi.uz/api/present/day?region=Samarqand").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    await call.message.answer_photo(img, f'<b>(Samarqand shahri)</b> namoz vaqti {today}\n\n'
                                         f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                         f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                         f'-------------------------------------\n'
                                         f'🕢 Bomdod          {bomdod}\n'
                                         f'-------------------------------------\n'
                                         f'☀ Quyosh            {quyosh}\n'
                                         f'-------------------------------------\n'
                                         f'🕑 Peshin              {peshin}\n'
                                         f'-------------------------------------\n'
                                         f'🕓 Asr                    {asr}\n'
                                         f'-------------------------------------\n'
                                         f'🕠 Shom                {shom}\n'
                                         f'-------------------------------------\n'
                                         f'🕖 Hufton             {xufton}\n'
                                         f'-------------------------------------\n'
                                         f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                         f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                         f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                         f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', reply_markup=ulashish, parse_mode='HTML')
    us_id = await db.select_user(telegram_id=call.message.chat.id)
    await db.update_user_region(user_region='Samarqand', telegram_id=us_id[3])
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='Sirdaryo')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    data = requests.get("https://islomapi.uz/api/present/day?region=Guliston").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    await call.message.answer_photo(img, f'<b>(Sirdaryo shahri)</b> namoz vaqti {today}\n\n'
                                         f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
                                         f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
                                         f'-------------------------------------\n'
                                         f'🕢 Bomdod          {bomdod}\n'
                                         f'-------------------------------------\n'
                                         f'☀ Quyosh            {quyosh}\n'
                                         f'-------------------------------------\n'
                                         f'🕑 Peshin              {peshin}\n'
                                         f'-------------------------------------\n'
                                         f'🕓 Asr                    {asr}\n'
                                         f'-------------------------------------\n'
                                         f'🕠 Shom                {shom}\n'
                                         f'-------------------------------------\n'
                                         f'🕖 Hufton             {xufton}\n'
                                         f'-------------------------------------\n'
                                         f'<i>Jobir ibn Abdulloh roziyallohu anhudan rivoyat qilinadi: </i>\n\n'
                                         f'📜 «Rosululloh sollallohu alayhi vasallam aytdilar» :\n'
                                         f'«Jannatning kaliti – namoz\nNamozning kaliti – tahorat»\n\n'
                                         f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>', reply_markup=ulashish, parse_mode='HTML')
    us_id = await db.select_user(telegram_id=call.message.chat.id)
    await db.update_user_region(user_region='Guliston', telegram_id=us_id[3])
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)





