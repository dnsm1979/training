import telebot
from telebot import types
from http.client import HTTPSConnection
from json import dumps, loads


bot = telebot.TeleBot("6636364771:AAH0UK8wIMPfLsYIxGEgWjtHd1S0sUZrKGI")
API_TOKEN = 'cadbf00e-3f47-474b-9da9-bbf17a4df82a'


result_ls = ['Орел', 'Решка']
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Выберете пожалуйста орел или решку!')
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Орел!", callback_data="heads")
    button2 = types.InlineKeyboardButton(text="Решка!", callback_data="tails")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Сделайте ваш выбор", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback_query: True)
def callback(call):
    if call.data == "heads":
        user_numbers = 1

    elif call.data == "tails":
        user_numbers = 2

    # bot.send_message(call.message.chat.id, user_numbers)
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
    # bot.send_message(call.message.chat.id, result)
    if result == user_numbers:
        bot.send_message(call.message.chat.id, f'Выпал {result_ls[result - 1]}, Вы победили!')
    else:
        bot.send_message(call.message.chat.id, f'Выпал {result_ls[result - 1]}, Вы проиграли!')




bot.polling(none_stop=True)