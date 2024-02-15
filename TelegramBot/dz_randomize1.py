import telebot
from telebot import types
from http.client import HTTPSConnection
from json import dumps, loads

bot = telebot.TeleBot("6636364771:AAH0UK8wIMPfLsYIxGEgWjtHd1S0sUZrKGI")
API_TOKEN = 'cadbf00e-3f47-474b-9da9-bbf17a4df82a'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Выберете диапозон чисел!')
    bot.send_message(
        message.chat.id,
        "Введите начальное число")
    bot.register_next_step_handler(message, user_number1)

def user_number1(message):
    global user_number1
    user_number1 = message.text.strip()
    bot.send_message(
        message.chat.id, 'Введите конечное число')
    bot.register_next_step_handler(message, user_number2)

def user_number2(message):
    global user_number2
    user_number2 = message.text.strip()

    request_data = {'jsonrpc': '2.0','method': 'generateIntegers','params': {
        'apiKey': API_TOKEN,'min': user_number1,'max': user_number2,'n': 1,},'id': 1,
                    }
    encoded_data = dumps(request_data)
    headers = {'Content-Type': 'application/json-rpc',}
    encoded_headers = dumps(headers)

    connection = HTTPSConnection('api.random.org')
    connection.request('GET', '/json-rpc/1/invoke', encoded_data, headers)
    response = connection.getresponse()
    response_data = loads(response.read().decode())
    bot.reply_to(message, f'Случайное число диапозона: {response_data["result"]["random"]["data"][0]}')



bot.polling(none_stop=True)