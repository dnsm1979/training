import telebot
from telebot import types
from http.client import HTTPSConnection
from json import dumps, loads
import time

from telebot.types import InlineKeyboardMarkup

bot = telebot.TeleBot("6636364771:AAH0UK8wIMPfLsYIxGEgWjtHd1S0sUZrKGI")
API_TOKEN = 'cadbf00e-3f47-474b-9da9-bbf17a4df82a'

ls_score = []
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! ')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Бросаем кости!", callback_data="start"))
    bot.send_message(message.chat.id, "Сыграем в кости!", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback(call):
    request_data = {'jsonrpc': '2.0','method': 'generateIntegers','params': {
        'apiKey': API_TOKEN,'min': 1,'max': 6,'n': 4,},'id': 1,
                    }
    encoded_data = dumps(request_data)
    headers = {'Content-Type': 'application/json-rpc',}
    encoded_headers = dumps(headers)

    connection = HTTPSConnection('api.random.org')
    connection.request('GET', '/json-rpc/1/invoke', encoded_data, headers)
    response = connection.getresponse()
    response_data = loads(response.read().decode())
    ls_score.append(response_data["result"]["random"]["data"][0])
    ls_score.append(response_data["result"]["random"]["data"][1])
    ls_score.append(response_data["result"]["random"]["data"][2])
    ls_score.append(response_data["result"]["random"]["data"][3])
    bot.send_message(call.message.chat.id, f'Ваш результат: {ls_score[0]}+{ls_score[1]}')
    time.sleep(3)
    bot.send_message(call.message.chat.id, 'Теперь кидаю я!')
    time.sleep(3)
    bot.send_message(call.message.chat.id, f'Мой результат: {ls_score[2]}+{ls_score[3]}')
    # result1 = response_data["result"]["random"]["data"][0]
    # result2 = response_data["result"]["random"]["data"][1]
    # result3 = response_data["result"]["random"]["data"][2]
    # result4 = response_data["result"]["random"]["data"][3]
    if ls_score[0] + ls_score[1] == ls_score[2] + ls_score[3]:
        bot.send_message(call.message.chat.id, f'{ls_score[0]}+{ls_score[1]} против {ls_score[2]}+{ls_score[3]}: Розыгрыш!')
    elif ls_score[0] + ls_score[1] < ls_score[2] + ls_score[3]:
        bot.send_message(call.message.chat.id, f'{ls_score[0]}+{ls_score[1]} против {ls_score[2]}+{ls_score[3]}: Вы проиграли!')
    else:
        bot.send_message(call.message.chat.id, f'{ls_score[0]}+{ls_score[1]} против {ls_score[2]}+{ls_score[3]}: Вы выйграли!')
    ls_score.clear()
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Играем!", callback_data="start")
    button2 = types.InlineKeyboardButton("Отмена!", callback_data="stop")
    markup.add(button1, button2)
    bot.send_message(call.message.chat.id, "Сыграем ещё?", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback(call):
    if callback.data == "stop":
        bot.send_message(call.message.chat.id, f'До свидания!')

    elif callback.data == "start":
        bot.send_message(call.message.chat.id, f'Отлично!')



bot.polling(none_stop=True)