import telebot
from telebot import types
from http.client import HTTPSConnection
from json import dumps, loads

from telebot.types import InlineKeyboardMarkup

bot = telebot.TeleBot("6636364771:AAH0UK8wIMPfLsYIxGEgWjtHd1S0sUZrKGI")
API_TOKEN = 'cadbf00e-3f47-474b-9da9-bbf17a4df82a'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Выберете пожалуйста 1-орел, 2-решка!')
    bot.send_message(
        message.chat.id,
        "Введите 1 или 2")
    bot.register_next_step_handler(message, user_number)

def user_number(message):
    global user_number
    user_number = message.text.strip()

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
    if result == int(user_number):
        bot.reply_to(message, f'Выпал {result}, Вы победили!')
    else:
        bot.reply_to(message, f'Выпал {result}, Вы проиграли!')

    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Играем!", callback_data=start)
    button2 = types.InlineKeyboardButton("Отмена!", url='https://habr.com/ru/all/')
    markup.add(button1, button2)
    bot.send_message(message.chat.id,
                     "{0.first_name}! Сыграем ещё?".format(message.from_user),
                     reply_markup=markup)



bot.polling(none_stop=True)