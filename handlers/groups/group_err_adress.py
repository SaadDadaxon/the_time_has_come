from keyboards.inline.inline import uzgargan_menu
from loader import dp, bot, db
from aiogram import types
from filters.group_filter import IsGroup, IsGroupCall


@dp.message_handler(IsGroup(), text='/guruh_manzili')
async def manzili(ms: types.Message):
    await bot.send_message(chat_id=ms.chat.id, text=f"Manzilingizni kiriting!", reply_markup=uzgargan_menu)


@dp.callback_query_handler(IsGroupCall(), text_contains="Tosh_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_group_region(group_region='Toshkent', group_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Guruhning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Andi_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_group_region(group_region='Andijon', group_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Guruhning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Bux_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_group_region(group_region='Buxoro', group_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Guruhning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Farg_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_group_region(group_region="Farg'ona", group_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Sizning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Jiz_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_group_region(group_region='Jizzax', group_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Guruhning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Xora_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_group_region(group_region='Xorazm', group_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Guruhning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Nam_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_group_region(group_region='Namangan', group_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Guruhning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Nav_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_group_region(group_region='Navoi', group_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Guruhning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Qash_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_group_region(group_region='Qarshi', group_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Guruhning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Qora_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_group_region(group_region='Nukus', group_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Guruhning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Samar_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_group_region(group_region='Samarqand', group_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Guruhning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)


@dp.callback_query_handler(IsGroupCall(), text_contains="Sir_err")
async def toshkent(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    await db.update_group_region(group_region='Guliston', group_id=chat_id)
    await bot.send_message(chat_id=chat_id, text="Guruhning Nomoz Vaqtlarini Kuzatib Boradigan Manzilingiz O'zgartirildi✅")
    await bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
