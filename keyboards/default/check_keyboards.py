from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

check_keyboards = ReplyKeyboardMarkup([
    [
        KeyboardButton("/crypto")
    ],
[
        KeyboardButton("/valute")
    ]
], resize_keyboard=True)