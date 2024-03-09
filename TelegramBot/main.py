import random

from telebot import types
import telebot

dict_bot = {
    "привет": "Привет!",
    "пока": "До свидания!",
    "как дела?": "Прекрасно!",
    "расскажи о себе": "Я бот!",
    "кто ты?": "я суперБОТ!",
}
writer = ["Шекспир", "Толстой", "Блок", "Донцова"]
poet = ["Пушкин", "Лермонтов", "Есенин", "Ахматова"]
book = ["Анна Коренина", "Ромео и джульета", "Герой нашего времени", "Война и мир"]
monologue = ["Первый монолог", "Второй монолог", "Третий монолог", "Четвертый монолог"]


bot = telebot.TeleBot("6636364771:AAH0UK8wIMPfLsYIxGEgWjtHd1S0sUZrKGI")


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Выставить лот на продажу")
    markup.row(btn1)
    btn2 = types.KeyboardButton("Посмотреть список вещей на продаже")
    markup.row(btn2)
    bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=markup)


@bot.message_handler(commands=["help"])
def main(message):
    bot.send_message(
        message.chat.id,
        "По всем вопросом обращайтесь в службу поддержки!",
        parse_mode="html",
    )


@bot.message_handler(content_types=["photo"])
def photos(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(
        "Перейти к заполнению формы", url="https://google.com"
    )
    btn2 = types.InlineKeyboardButton(
        "Отменить проверку", callback_data="cancel_checkin"
    )
    markup.row(btn1, btn2)
    bot.reply_to(message, "Фото отправлено на проверку!", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "cancel_checkin":
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)


@bot.message_handler()
def get_text_messages(message):
    x = message.text.lower()
    if x == "писатель":
        bot.send_message(message.chat.id, random.choice(writer))
    elif x == "поэт":
        bot.send_message(message.chat.id, random.choice(poet))
    elif x == "книга":
        bot.send_message(message.chat.id, random.choice(book))
    elif x == "монолог":
        bot.send_message(message.chat.id, random.choice(monologue))

    elif x in dict_bot:
        bot.send_message(message.chat.id, dict_bot[x])
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю!")


bot.polling(none_stop=True)
