import telebot
from telebot import types
import sqlite3


bot = telebot.TeleBot("6636364771:AAH0UK8wIMPfLsYIxGEgWjtHd1S0sUZrKGI")

name = None


@bot.message_handler(commands=["start"])
def start(message):
    conn = sqlite3.connect("telegram.sql")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER AUTO_INCREMENT PRIMARY KEY, name varchar(50), pass varchar(50))"
    )
    conn.commit()
    cursor.close()
    conn.close()

    bot.send_message(message.chat.id, "Регистрация. Введите имя")
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    name = message.text.strip()
    bot.send_message(message.chat.id, "Введите пароль")
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect("telegram.sql")
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO users (name,pass) VALUES("%s", "%s")' % (name, password)
    )

    conn.commit()
    cursor.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Список пользователей", callback_data="users")
    )
    bot.send_message(message.chat.id, "Регистрация завершена", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback(call):
    conn = sqlite3.connect("telegram.sql")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    info = ""

    for user in users:
        info += f"Имя: {user[1]}, Пароль: {user[2]}\n"
    cursor.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)
