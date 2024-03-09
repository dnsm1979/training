import telebot
from telebot import types
import requests
import json

bot = telebot.TeleBot("6636364771:AAH0UK8wIMPfLsYIxGEgWjtHd1S0sUZrKGI")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! В каком городе нужно узнать погоду?")


@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=3d9de74844d28377e81415151cbe6a66"
    )
    data = json.loads(res.text)
    bot.reply_to(message, f'Сейчас в этом городе: {data["name"]["temp"]} градусов')


bot.polling(none_stop=True)
