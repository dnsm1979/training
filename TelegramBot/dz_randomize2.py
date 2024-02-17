import telebot
from telebot import types
from http.client import HTTPSConnection
from json import dumps, loads

from telebot.types import InlineKeyboardMarkup

bot = telebot.TeleBot("6636364771:AAH0UK8wIMPfLsYIxGEgWjtHd1S0sUZrKGI")
API_TOKEN = 'cadbf00e-3f47-474b-9da9-bbf17a4df82a'

user_ls = []
result_ls = ['Орел', 'Решка']
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Выберете пожалуйста орел или решку!')
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Орел!", callback_data="heads")
    button2 = types.InlineKeyboardButton("Решка!", callback_data="tails")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Сделайте ваш выбор", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback(call):
    if callback == "heads":
        user_ls.append(1)

    elif callback == "tails":
        user_ls.append(2)

    user_number = user_ls
    request_data = {'jsonrpc': '2.0','method': 'generateIntegers','params': {
        'apiKey': API_TOKEN,'min': 1,'max': 2,'n': 1,},'id': 1,
                    }
    encoded_data = dumps(request_data)
    headers = {'Content-Type': 'application/json-rpc',}
    encoded_headers = dumps(headers)

    connection = HTTPSConnection('api.random.org')
    connection.request('GET', '/json-rpc/1/invoke', encoded_data, headers)
    response = connection.getresponse()
    response_data = loads(response.read().decode())
    result = response_data["result"]["random"]["data"][0]
    bot.reply_to(call.message, result)
    if result == user_ls:
        bot.reply_to(call.message, f'Выпал {result_ls[result - 1]}, Вы победили!')
    else:
        bot.reply_to(call.message, f'Выпал {result_ls[result - 1]}, Вы проиграли!')

    user_ls.clear()



bot.polling(none_stop=True)