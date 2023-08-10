from keyboards.inline.inline import uzgargan_menu
from loader import dp, bot, db
from aiogram import types
from filters.private_filter import IsPrivate, IsPrivates


@dp.message_handler(IsPrivates(), text='/foydalanuvchining_manzili')
async def manzili(ms: types.Message):
    await bot.send_message(chat_id=ms.chat.id, text=f"Manzilingizni kiriting!", reply_markup=uzgargan_menu)


@dp.callback_query_handler(IsPrivate(), text_contains="Tosh_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_user_region(user_region='Toshkent', telegram_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Sizning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains="Andi_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_user_region(user_region='Andijon', telegram_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Sizning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains="Bux_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_user_region(user_region='Buxoro', telegram_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Sizning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains="Farg_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_user_region(user_region="Farg'ona", telegram_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Sizning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains="Jiz_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_user_region(user_region='Jizzax', telegram_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Sizning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains="Xora_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_user_region(user_region='Xorazm', telegram_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Sizning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains="Nam_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_user_region(user_region='Namangan', telegram_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Sizning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains="Nav_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_user_region(user_region='Navoi', telegram_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Sizning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains="Qash_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_user_region(user_region='Qarshi', telegram_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Sizning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains="Qora_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_user_region(user_region='Nukus', telegram_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Sizning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains="Samar_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_user_region(user_region='Samarqand', telegram_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Sizning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsPrivate(), text_contains="Sir_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_user_region(user_region='Guliston', telegram_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Sizning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
