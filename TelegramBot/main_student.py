import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot("6636364771:AAH0UK8wIMPfLsYIxGEgWjtHd1S0sUZrKGI")

username = None
age = None


@bot.message_handler(commands=["start"])
def start(message):
    conn = sqlite3.connect("students_db.sql")
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS students (id INTEGER AUTO_INCREMENT PRIMARY KEY, username varchar(50), age integer, average  real)')
    conn.commit()
    cursor.close()
    conn.close()

    bot.send_message(
        message.chat.id,
        "Регистрация. Введите имя")
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global username
    username = message.text.strip()
    bot.send_message(
        message.chat.id, 'Введите возраст')
    bot.register_next_step_handler(message, user_age)


def user_age(message):
    global age
    age = message.text.strip()
    bot.send_message(
        message.chat.id, 'Введите средний балл')
    bot.register_next_step_handler(message, user_average)


def user_average(message):
    average = message.text.strip()

    conn = sqlite3.connect("students_db.sql")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (username,age,average) VALUES("%s", "%s", "%s")' % (username, age, average))

    conn.commit()
    cursor.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Список студентов", callback_data="students"))
    bot.send_message(message.chat.id, "Регистрация завершена", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback(call):
    conn = sqlite3.connect("students_db.sql")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students WHERE average > 4')
    students = cursor.fetchall()
    info = ''

    for st in students:
        info += f'Имя: {st[1]}, возраст: {st[2]}, Средний балл: {st[3]}\n'
    cursor.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)
