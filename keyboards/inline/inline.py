from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging
from aiogram.utils.callback_data import CallbackData

viloyat_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Toshkent", callback_data="Toshkent"),
        ],
        [
            InlineKeyboardButton(text="Andijon", callback_data="Andijon"),
            InlineKeyboardButton(text="Buxoro", callback_data="Buxoro")
        ],
        [
            InlineKeyboardButton(text="Farg'ona", callback_data="Farg'ona"),
            InlineKeyboardButton(text="Jizzax", callback_data="Jizzax")
        ],
        [
            InlineKeyboardButton(text="Xorazm", callback_data="Xorazm"),
            InlineKeyboardButton(text="Namangan", callback_data="Namangan")
        ],
        [
            InlineKeyboardButton(text="Navoi", callback_data="Navoi"),
            InlineKeyboardButton(text="Qashqadaryo", callback_data="Qashqadaryo")
        ],
        [
            InlineKeyboardButton(text="Qoraqalpog'iston", callback_data="Qoraqalpog"),
            InlineKeyboardButton(text="Samarqand", callback_data="Samarqand")
        ],
        [
            InlineKeyboardButton(text="Sirdaryo", callback_data="Sirdaryo"),
        ],
    ]
)


uzgargan_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Toshkent", callback_data="Tosh_err"),
        ],
        [
            InlineKeyboardButton(text="Andijon", callback_data="Andi_err"),
            InlineKeyboardButton(text="Buxoro", callback_data="Bux_err")
        ],
        [
            InlineKeyboardButton(text="Farg'ona", callback_data="Farg_err"),
            InlineKeyboardButton(text="Jizzax", callback_data="Jiz_err")
        ],
        [
            InlineKeyboardButton(text="Xorazm", callback_data="Xora_err"),
            InlineKeyboardButton(text="Namangan", callback_data="Nam_err")
        ],
        [
            InlineKeyboardButton(text="Navoi", callback_data="Nav_err"),
            InlineKeyboardButton(text="Qashqadaryo", callback_data="Qash_err")
        ],
        [
            InlineKeyboardButton(text="Qoraqalpog'iston", callback_data="Qora_err"),
            InlineKeyboardButton(text="Samarqand", callback_data="Samar_err")
        ],
        [
            InlineKeyboardButton(text="Sirdaryo", callback_data="Sir_err"),
        ],
    ]
)

rus_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Moscow", callback_data="moscow"),
        ],
        [
            InlineKeyboardButton(text="Belgorod", callback_data="belgorod"),
            InlineKeyboardButton(text="Bryansk", callback_data="bryansk")
        ],
        [
            InlineKeyboardButton(text="Vladimir", callback_data="vladimir"),
            InlineKeyboardButton(text="Ivanovo", callback_data="ivanovo")
        ],
        [
            InlineKeyboardButton(text="Ryazan", callback_data="ryazan"),
            InlineKeyboardButton(text="Oryol", callback_data="oryol")
        ],
        [
            InlineKeyboardButton(text="Tula", callback_data="tula")
        ]
    ]
)

joy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿Uzbekiston", callback_data='uzbek'),
            InlineKeyboardButton(text="🇷🇺Rossiya", callback_data='russ')
        ]
    ]
)

post_callback = CallbackData('create_post', 'action')

confirmation = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🆗 Chop etish", callback_data=post_callback.new(action='post')),
            InlineKeyboardButton(text="🚫 Rad etish", callback_data=post_callback.new(action='cancel')),
        ]
    ]
)

ulashish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Botni Ulashish', switch_inline_query='')
        ]
    ]
)
