from aiogram.types import message
from pycbrf import ExchangeRates

from loader import dp, client
import time


@dp.message_handler(commands="crypto", state="*")
async def crypto(call: message.Message):
    time_here = time.strftime("%d.%m.%Y %H:%M:%S")



    await call.answer("КРИПТОВАЛЮТа\n"
                      f"🕐Время проверки: {time_here}\n\n"
                      f"✅Monero(XMR): {get_plus('XMR')}\n\n"
                      f"✅Solana(SOL): {get_plus('SOL')}\n\n"
                      f"✅BNB(BNB): {get_plus('BNB')}\n\n"
                      f"✅TRON(TRX): {get_plus('TRX')}\n\n"
                      f"✅Terra(LUNA): {get_plus('LUNA')}\n\n"
                      f"✅Dogecoin(DOGE): {round(0.3074446680080483, 3)}"
                      )


def get_plus(crypto):
    my_trades = float(client.get_my_trades(symbol=f'{crypto}USDT')[0]['price'])
    get_avg_price = float(client.get_avg_price(symbol=f'{crypto}USDT')['price'])
    get_avg_price = round(get_avg_price, 3)
    percent = (get_avg_price - my_trades) / my_trades * 100
    percent = round(percent, 3)
    return f' {get_avg_price}$ {arrow(percent)}{percent}%'


currency = {
    'avg_price': {
        "USD": [77.88, 74.23, 74.41, 74.57, 78.16, 78.11],
        "EUR": [92.50, 91.13, 90.99]
    },
    'count': {
        "USD": [500, 1000, 500, 1000, 1000, 1000],
        "EUR": [140, 400, 460]
    }
}


def arrow(percent_2):
    if percent_2 <= 0:
        return "⬇"
    else:
        return "⬆"

@dp.message_handler(commands="valute", state="*")
async def crypto(call: message.Message):
    time_here = time.strftime("%d.%m.%Y %H:%M:%S")
    time_v = time.strftime("%Y-%m-%d")

    def culc_currency(sub_currency, operation):
        if operation == "request_bank":
            return float(ExchangeRates(time_v, locale_en=True)[sub_currency].value)
        if operation == "avg_price":
            return sum(currency['avg_price'][sub_currency]) / len(currency['avg_price'][sub_currency])
        if operation == "percent":
           return round((culc_currency(sub_currency, "request_bank") - culc_currency(sub_currency, "avg_price")) / culc_currency(sub_currency, "avg_price") * 100,
                        2)


    await call.answer("💱ВАЛЮТА💱\n"
                      f"🕐{time_here}\n\n"

                      f"💵USD: {round(culc_currency('USD', 'request_bank') * sum(currency['count']['USD']), 2)} руб. {arrow(culc_currency('USD', 'percent'))}{culc_currency('USD', 'percent')}%\n"
                      f"🏦курс ЦБ: {round(culc_currency('USD', 'request_bank'), 2)}\n"
                      f"Закуп по: {round(culc_currency('USD', 'avg_price'), 2)}\n\n"

                      f"💶EUR: {round(culc_currency('EUR', 'request_bank') * sum(currency['count']['EUR']), 2)} руб. {arrow(culc_currency('EUR', 'percent'))}{culc_currency('EUR', 'percent')}%\n"
                      f"🏦курс ЦБ: {round(culc_currency('EUR', 'request_bank'), 2)}\n"
                      f"Закуп по: {round(culc_currency('EUR', 'avg_price'), 2)}\n\n"
                      )
