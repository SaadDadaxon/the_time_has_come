import asyncio
from datetime import datetime, timedelta
import requests
from filters.group_filter import IsGroup, IsGroupCall
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot


@dp.callback_query_handler(IsGroupCall(), text_contains='Toshkent')
async def region_tanlash(call: types.CallbackQuery):
    gr_id = await db.select_group(group_id=call.message.chat.id)
    await db.update_group_region(group_region="Toshkent", group_id=gr_id[2])  # group_id ni o'rniga tegishli o'zgaruvchini kiritish
    group_id = await db.select_group(group_id=call.message.chat.id)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    ertangi_kun = today + timedelta(days=1)
    data = requests.get(f"https://islomapi.uz/api/present/day?region={group_id[3]}").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    msg = f'<b>({group_id[3]} shahri)</b> namoz vaqti {ertangi_kun}\n\n'
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
    msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>'
    await bot.send_photo(chat_id=group_id[2], photo=img, caption=msg, parse_mode='HTML')
    await asyncio.sleep(0.05)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains='Buxoro')
async def region_tanlash(call: types.CallbackQuery):
    gr_id = await db.select_group(group_id=call.message.chat.id)
    await db.update_group_region(group_region="Buxoro", group_id=gr_id[2])  # group_id ni o'rniga tegishli o'zgaruvchini kiritish
    group_id = await db.select_group(group_id=call.message.chat.id)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    ertangi_kun = today + timedelta(days=1)
    data = requests.get(f"https://islomapi.uz/api/present/day?region={group_id[3]}").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    msg = f'<b>({group_id[3]} shahri)</b> namoz vaqti {ertangi_kun}\n\n'
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
    msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>'
    await bot.send_photo(chat_id=group_id[2], photo=img, caption=msg, parse_mode='HTML')
    await asyncio.sleep(0.05)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains='Andijon')
async def region_tanlash(call: types.CallbackQuery):
    gr_id = await db.select_group(group_id=call.message.chat.id)
    await db.update_group_region(group_region="Andijon", group_id=gr_id[2])  # group_id ni o'rniga tegishli o'zgaruvchini kiritish
    group_id = await db.select_group(group_id=call.message.chat.id)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    ertangi_kun = today + timedelta(days=1)
    data = requests.get(f"https://islomapi.uz/api/present/day?region={group_id[3]}").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    msg = f'<b>({group_id[3]} shahri)</b> namoz vaqti {ertangi_kun}\n\n'
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
    msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>'
    await bot.send_photo(chat_id=group_id[2], photo=img, caption=msg, parse_mode='HTML')
    await asyncio.sleep(0.05)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Farg'ona")
async def region_tanlash(call: types.CallbackQuery):
    gr_id = await db.select_group(group_id=call.message.chat.id)
    await db.update_group_region(group_region="Farg'ona", group_id=gr_id[2])  # group_id ni o'rniga tegishli o'zgaruvchini kiritish
    group_id = await db.select_group(group_id=call.message.chat.id)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    ertangi_kun = today + timedelta(days=1)
    data = requests.get(f"https://islomapi.uz/api/present/day?region={group_id[3]}").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    msg = f'<b>({group_id[3]} shahri)</b> namoz vaqti {ertangi_kun}\n\n'
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
    msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>'
    await bot.send_photo(chat_id=group_id[2], photo=img, caption=msg, parse_mode='HTML')
    await asyncio.sleep(0.05)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Jizzax")
async def region_tanlash(call: types.CallbackQuery):
    gr_id = await db.select_group(group_id=call.message.chat.id)
    await db.update_group_region(group_region="Jizzax", group_id=gr_id[2])  # group_id ni o'rniga tegishli o'zgaruvchini kiritish
    group_id = await db.select_group(group_id=call.message.chat.id)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    ertangi_kun = today + timedelta(days=1)
    data = requests.get(f"https://islomapi.uz/api/present/day?region={group_id[3]}").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    msg = f'<b>({group_id[3]} shahri)</b> namoz vaqti {ertangi_kun}\n\n'
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
    msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>'
    await bot.send_photo(chat_id=group_id[2], photo=img, caption=msg, parse_mode='HTML')
    await asyncio.sleep(0.05)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Xorazm")
async def region_tanlash(call: types.CallbackQuery):
    gr_id = await db.select_group(group_id=call.message.chat.id)
    await db.update_group_region(group_region="Xorazm", group_id=gr_id[2])  # group_id ni o'rniga tegishli o'zgaruvchini kiritish
    group_id = await db.select_group(group_id=call.message.chat.id)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    ertangi_kun = today + timedelta(days=1)
    data = requests.get(f"https://islomapi.uz/api/present/day?region={group_id[3]}").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    msg = f'<b>({group_id[3]} shahri)</b> namoz vaqti {ertangi_kun}\n\n'
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
    msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>'
    await bot.send_photo(chat_id=group_id[2], photo=img, caption=msg, parse_mode='HTML')
    await asyncio.sleep(0.05)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Namangan")
async def region_tanlash(call: types.CallbackQuery):
    gr_id = await db.select_group(group_id=call.message.chat.id)
    await db.update_group_region(group_region="Namangan", group_id=gr_id[2])  # group_id ni o'rniga tegishli o'zgaruvchini kiritish
    group_id = await db.select_group(group_id=call.message.chat.id)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    ertangi_kun = today + timedelta(days=1)
    data = requests.get(f"https://islomapi.uz/api/present/day?region={group_id[3]}").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    msg = f'<b>({group_id[3]} shahri)</b> namoz vaqti {ertangi_kun}\n\n'
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
    msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>'
    await bot.send_photo(chat_id=group_id[2], photo=img, caption=msg, parse_mode='HTML')
    await asyncio.sleep(0.05)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Navoi")
async def region_tanlash(call: types.CallbackQuery):
    gr_id = await db.select_group(group_id=call.message.chat.id)
    await db.update_group_region(group_region="Navoi", group_id=gr_id[2])  # group_id ni o'rniga tegishli o'zgaruvchini kiritish
    group_id = await db.select_group(group_id=call.message.chat.id)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    ertangi_kun = today + timedelta(days=1)
    data = requests.get(f"https://islomapi.uz/api/present/day?region={group_id[3]}").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    msg = f'<b>({group_id[3]} shahri)</b> namoz vaqti {ertangi_kun}\n\n'
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
    msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>'
    await bot.send_photo(chat_id=group_id[2], photo=img, caption=msg, parse_mode='HTML')
    await asyncio.sleep(0.05)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Qashqadaryo")
async def region_tanlash(call: types.CallbackQuery):
    gr_id = await db.select_group(group_id=call.message.chat.id)
    await db.update_group_region(group_region="Qarshi", group_id=gr_id[2])  # group_id ni o'rniga tegishli o'zgaruvchini kiritish
    group_id = await db.select_group(group_id=call.message.chat.id)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    ertangi_kun = today + timedelta(days=1)
    data = requests.get(f"https://islomapi.uz/api/present/day?region={group_id[3]}").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    msg = f'<b>({group_id[3]} shahri)</b> namoz vaqti {ertangi_kun}\n\n'
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
    msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>'
    await bot.send_photo(chat_id=group_id[2], photo=img, caption=msg, parse_mode='HTML')
    await asyncio.sleep(0.05)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Qoraqalpoq")
async def region_tanlash(call: types.CallbackQuery):
    gr_id = await db.select_group(group_id=call.message.chat.id)
    await db.update_group_region(group_region="Nukus", group_id=gr_id[2])  # group_id ni o'rniga tegishli o'zgaruvchini kiritish
    group_id = await db.select_group(group_id=call.message.chat.id)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    ertangi_kun = today + timedelta(days=1)
    data = requests.get(f"https://islomapi.uz/api/present/day?region={group_id[3]}").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    msg = f'<b>({group_id[3]} shahri)</b> namoz vaqti {ertangi_kun}\n\n'
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
    msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>'
    await bot.send_photo(chat_id=group_id[2], photo=img, caption=msg, parse_mode='HTML')
    await asyncio.sleep(0.05)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Samarqand")
async def region_tanlash(call: types.CallbackQuery):
    gr_id = await db.select_group(group_id=call.message.chat.id)
    await db.update_group_region(group_region="Samarqand", group_id=gr_id[2])  # group_id ni o'rniga tegishli o'zgaruvchini kiritish
    group_id = await db.select_group(group_id=call.message.chat.id)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    ertangi_kun = today + timedelta(days=1)
    data = requests.get(f"https://islomapi.uz/api/present/day?region={group_id[3]}").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    msg = f'<b>({group_id[3]} shahri)</b> namoz vaqti {ertangi_kun}\n\n'
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
    msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>'
    await bot.send_photo(chat_id=group_id[2], photo=img, caption=msg, parse_mode='HTML')
    await asyncio.sleep(0.05)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Sirdaryo")
async def region_tanlash(call: types.CallbackQuery):
    gr_id = await db.select_group(group_id=call.message.chat.id)
    await db.update_group_region(group_region="Guliston", group_id=gr_id[2])  # group_id ni o'rniga tegishli o'zgaruvchini kiritish
    group_id = await db.select_group(group_id=call.message.chat.id)
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.today().date()
    ertangi_kun = today + timedelta(days=1)
    data = requests.get(f"https://islomapi.uz/api/present/day?region={group_id[3]}").json()
    bomdod = data['times']['tong_saharlik']
    quyosh = data['times']['quyosh']
    peshin = data['times']['peshin']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    xufton = data['times']['hufton']
    msg = f'<b>({group_id[3]} shahri)</b> namoz vaqti {ertangi_kun}\n\n'
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
    msg += f'📚 <i>Abu Dovud rivoyat qilgan.</i></b>'
    await bot.send_photo(chat_id=group_id[2], photo=img, caption=msg, parse_mode='HTML')
    await asyncio.sleep(0.05)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
