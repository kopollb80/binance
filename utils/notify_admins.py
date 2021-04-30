import logging

from aiogram import Dispatcher

from data.config import ADMINS
from keyboards.default import check_keyboards


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен", reply_markup=check_keyboards)

        except Exception as err:
            logging.exception(err)
