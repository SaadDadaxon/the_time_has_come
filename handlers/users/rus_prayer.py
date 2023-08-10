from filters.private_filter import IsPrivate
import requests
from aiogram.types import Message, CallbackQuery
from loader import dp, bot, db
from keyboards.inline.inline import viloyat_menu, rus_menu, ulashish

import datetime


@dp.callback_query_handler(text_contains="russ")
async def vaqt(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    await call.message.answer_photo(img, reply_markup=rus_menu)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='moscow')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.datetime.today().date()
    data = requests.get("https://api.aladhan.com/v1/timingsByCity/15-06-2023?city=Moscow&country=Russia&method=8").json()
    bomdod = datetime.datetime.strptime(data['data']['timings']['Fajr'], "%H:%M")
    min = datetime.timedelta(minutes=25)
    yangi_bomdod = bomdod + min
    yangi_vaqt_bomdod = yangi_bomdod.strftime("%H:%M")
    quyosh = data['data']['timings']['Sunrise']
    peshin = data['data']['timings']['Dhuhr']
    asr = data['data']['timings']['Asr']
    shom = data['data']['timings']['Maghrib']
    xufton = data['data']['timings']['Isha']
    msg = f'<b>(Moscow shahri)</b> namoz vaqti {today}\n\n'
    msg += f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
    msg += f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
    msg += f'-------------------------------------\n'
    msg += f'🕢 Bomdod          {yangi_vaqt_bomdod}\n'
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
    await bot.send_photo(chat_id=call.from_user.id, photo=img, caption=msg, reply_markup=ulashish, parse_mode='HTML')
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='belgorod')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.datetime.today().date()
    data = requests.get("https://api.aladhan.com/v1/timingsByCity/15-06-2023?city=Belgorod&country=Russia&method=8").json()
    bomdod = datetime.datetime.strptime(data['data']['timings']['Fajr'], "%H:%M")
    min = datetime.timedelta(minutes=25)
    yangi_bomdod = bomdod + min
    yangi_vaqt_bomdod = yangi_bomdod.strftime("%H:%M")
    quyosh = data['data']['timings']['Sunrise']
    peshin = data['data']['timings']['Dhuhr']
    asr = data['data']['timings']['Asr']
    shom = data['data']['timings']['Maghrib']
    xufton = data['data']['timings']['Isha']
    msg = f'<b>(Belgorod shahri)</b> namoz vaqti {today}\n\n'
    msg += f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
    msg += f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
    msg += f'-------------------------------------\n'
    msg += f'🕢 Bomdod          {yangi_vaqt_bomdod}\n'
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
    await bot.send_photo(chat_id=call.from_user.id, photo=img, caption=msg, reply_markup=ulashish, parse_mode='HTML')
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='bryansk')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.datetime.today().date()
    data = requests.get("https://api.aladhan.com/v1/timingsByCity/15-06-2023?city=Bryansk&country=Russia&method=8").json()
    bomdod = datetime.datetime.strptime(data['data']['timings']['Fajr'], "%H:%M")
    min = datetime.timedelta(minutes=25)
    yangi_bomdod = bomdod + min
    yangi_vaqt_bomdod = yangi_bomdod.strftime("%H:%M")
    quyosh = data['data']['timings']['Sunrise']
    peshin = data['data']['timings']['Dhuhr']
    asr = data['data']['timings']['Asr']
    shom = data['data']['timings']['Maghrib']
    xufton = data['data']['timings']['Isha']
    msg = f'<b>(Bryansk shahri)</b> namoz vaqti {today}\n\n'
    msg += f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
    msg += f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
    msg += f'-------------------------------------\n'
    msg += f'🕢 Bomdod          {yangi_vaqt_bomdod}\n'
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
    await bot.send_photo(chat_id=call.from_user.id, photo=img, caption=msg, reply_markup=ulashish, parse_mode='HTML')
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='vladimir')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.datetime.today().date()
    data = requests.get("https://api.aladhan.com/v1/timingsByCity/15-06-2023?city=Vladimir&country=Russia&method=8").json()
    bomdod = datetime.datetime.strptime(data['data']['timings']['Fajr'], "%H:%M")
    min = datetime.timedelta(minutes=25)
    yangi_bomdod = bomdod + min
    yangi_vaqt_bomdod = yangi_bomdod.strftime("%H:%M")
    quyosh = data['data']['timings']['Sunrise']
    peshin = data['data']['timings']['Dhuhr']
    asr = data['data']['timings']['Asr']
    shom = data['data']['timings']['Maghrib']
    xufton = data['data']['timings']['Isha']
    msg = f'<b>(Vladimir shahri)</b> namoz vaqti {today}\n\n'
    msg += f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
    msg += f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
    msg += f'-------------------------------------\n'
    msg += f'🕢 Bomdod          {yangi_vaqt_bomdod}\n'
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
    await bot.send_photo(chat_id=call.from_user.id, photo=img, caption=msg, reply_markup=ulashish, parse_mode='HTML')
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='ivanovo')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.datetime.today().date()
    data = requests.get("https://api.aladhan.com/v1/timingsByCity/15-06-2023?city=Ivanovo&country=Russia&method=8").json()
    bomdod = datetime.datetime.strptime(data['data']['timings']['Fajr'], "%H:%M")
    min = datetime.timedelta(minutes=25)
    yangi_bomdod = bomdod + min
    yangi_vaqt_bomdod = yangi_bomdod.strftime("%H:%M")
    quyosh = data['data']['timings']['Sunrise']
    peshin = data['data']['timings']['Dhuhr']
    asr = data['data']['timings']['Asr']
    shom = data['data']['timings']['Maghrib']
    xufton = data['data']['timings']['Isha']
    msg = f'<b>(Ivanovo shahri)</b> namoz vaqti {today}\n\n'
    msg += f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
    msg += f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
    msg += f'-------------------------------------\n'
    msg += f'🕢 Bomdod          {yangi_vaqt_bomdod}\n'
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
    await bot.send_photo(chat_id=call.from_user.id, photo=img, caption=msg, reply_markup=ulashish, parse_mode='HTML')
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='ryazan')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.datetime.today().date()
    data = requests.get("https://api.aladhan.com/v1/timingsByCity/15-06-2023?city=Ryazan&country=Russia&method=8").json()
    bomdod = datetime.datetime.strptime(data['data']['timings']['Fajr'], "%H:%M")
    min = datetime.timedelta(minutes=25)
    yangi_bomdod = bomdod + min
    yangi_vaqt_bomdod = yangi_bomdod.strftime("%H:%M")
    quyosh = data['data']['timings']['Sunrise']
    peshin = data['data']['timings']['Dhuhr']
    asr = data['data']['timings']['Asr']
    shom = data['data']['timings']['Maghrib']
    xufton = data['data']['timings']['Isha']
    msg = f'<b>(Ryazan shahri)</b> namoz vaqti {today}\n\n'
    msg += f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
    msg += f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
    msg += f'-------------------------------------\n'
    msg += f'🕢 Bomdod          {yangi_vaqt_bomdod}\n'
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
    await bot.send_photo(chat_id=call.from_user.id, photo=img, caption=msg, reply_markup=ulashish, parse_mode='HTML')
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='oryol')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.datetime.today().date()
    data = requests.get("https://api.aladhan.com/v1/timingsByCity/15-06-2023?city=Oryol&country=Russia&method=8").json()
    bomdod = datetime.datetime.strptime(data['data']['timings']['Fajr'], "%H:%M")
    min = datetime.timedelta(minutes=25)
    yangi_bomdod = bomdod + min
    yangi_vaqt_bomdod = yangi_bomdod.strftime("%H:%M")
    quyosh = data['data']['timings']['Sunrise']
    peshin = data['data']['timings']['Dhuhr']
    asr = data['data']['timings']['Asr']
    shom = data['data']['timings']['Maghrib']
    xufton = data['data']['timings']['Isha']
    msg = f'<b>(Oryol shahri)</b> namoz vaqti {today}\n\n'
    msg += f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
    msg += f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
    msg += f'-------------------------------------\n'
    msg += f'🕢 Bomdod          {yangi_vaqt_bomdod}\n'
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
    await bot.send_photo(chat_id=call.from_user.id, photo=img, caption=msg, reply_markup=ulashish, parse_mode='HTML')
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains='tula')
async def toshkent_time(call: CallbackQuery):
    img = open("image/photo_2022-11-13_22-40-34.jpg", "rb")
    today = datetime.datetime.today().date()
    data = requests.get("https://api.aladhan.com/v1/timingsByCity/15-06-2023?city=Tula&country=Russia&method=8").json()
    bomdod = datetime.datetime.strptime(data['data']['timings']['Fajr'], "%H:%M")
    min = datetime.timedelta(minutes=25)
    yangi_bomdod = bomdod + min
    yangi_vaqt_bomdod = yangi_bomdod.strftime("%H:%M")
    quyosh = data['data']['timings']['Sunrise']
    peshin = data['data']['timings']['Dhuhr']
    asr = data['data']['timings']['Asr']
    shom = data['data']['timings']['Maghrib']
    xufton = data['data']['timings']['Isha']
    msg = f'<b>(Tula shahri)</b> namoz vaqti {today}\n\n'
    msg += f'<b> إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا\n\n'
    msg += f'...Albatta namoz mo\'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)\n'
    msg += f'-------------------------------------\n'
    msg += f'🕢 Bomdod          {yangi_vaqt_bomdod}\n'
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
    await bot.send_photo(chat_id=call.from_user.id, photo=img, caption=msg, reply_markup=ulashish, parse_mode='HTML')
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
