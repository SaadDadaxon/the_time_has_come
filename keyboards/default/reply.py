from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging

bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📖Quron'),
            KeyboardButton(text='📜Hadis')
        ],
        [
            KeyboardButton(text='🕰Nomoz Vaqtlari'),
            KeyboardButton(text="📜Hadis qo'shish➕")
        ]
        # [
        #     KeyboardButton(text='⚙Bot Haqida')
        # ]
    ],
    resize_keyboard=True
)

info_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝Bot Ma'lumoti"),
            KeyboardButton(text="🧔Bot Yaratuvchisi💻")
        ],
        [
            KeyboardButton(text='⏪Ortga')
        ]
    ],
    resize_keyboard=True
)
