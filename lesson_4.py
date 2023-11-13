# string = 'Hello'
# encoded_string = string.encode(encoding='utf8')
# print(encoded_string)
# decoded_string = encoded_string.decode(encoding='utf8')
# print(decoded_string)

string = 'abcdefg'
# print(len(string))
# print(string[0])
# print(string[-1])
# print(string[len(string) - 1])
# print(string[0:3])
# print(string[:3])
# print(string[3:])
#print(string[0:5:2])
# print(string[-1:-4:-1])
# print(string[::-1])

# example = '0123456789'
# print(example[:3])
# print(example[3:6])
# print(example[-1:-4:-1])
# print(example[::2])
# print(example[-1::-1])
# print(example[5:2:-1])
# print(example[-2:3:-2])
# print(example[4:0:-1])

# text = 'pytHon is a progrAmming language'
# print(text.capitalize()) # Первый символ в верхнем регистре
# print(text.title()) # Каждое слово с заглавной буквы
# print(text.count('p')) # Количество последовательносьей в строке
# print(text.lower()) # все в нижнем регистре
# print(text.upper()) # Все в верхнем регистре
#print(text.replace(' ', '-')) # замена символов
# print(text.index('n')) # индекс символа
# print(text.find('ж'))print(text.find('ж')) #
# print(len(text))
# print(len(text.rstrip()))
# print(text.swapcase())
#string_2 = 'Python123@ruby78.ru'
# print(string_2.isalnum())
# print(string_2.isalpha()) # Проверка, Только из букв
# print(string_2.isdigit()) # Проверка , только из цифр
# print(string_2.islower()) # проверка на нижний регистр
# print(string_2.isupper()) # проверка на верхний регистр
# print(string_2.isascii()) # проверка на ascii
# print(string_2.isdecimal()) # проверка на целые числа в строке
# print(string_2.isnumeric()) # проверка на целые числа в строке
# print(string_2.isspace()) # проверка на пробелы
# print(string_2.startswith('P'))
# print(string_2.endswith('.ru')) # проверка на вхождение
#
# print('@' in string_2) # проверка на вхождение
# print(string_2.count('@') == 1) # проверка на вхождение

#string_3 = 'Python ruby js'
# print(string_3.split(''))

# string = input('Введите текст: ')
# print('Нижнего регистра: ', string.count('ы'))
# print('Верхнего регистра: ', string.count('Ы'))

# Email содержит (@, .ru, .com)
# Password содержит 8 символов, буквы и цифры, без спецсимволов
# регистрация пока не введет правильно

# registration = False
#
# while not registration:
#     email = input('Введите свой Email: ')
#     password_1 = input('Введите пароль: ')
#     password_2 = input('Подтвердите пароль: ')
#     if ('@' in email) and (email.endswith('.com') or email.endswith('.ru')):
#         if password_1 == password_2:
#             if len(password_1) == 8 and password_1.isalnum() and not password_1.isalpha() and not password_1.isdigit():
#                 print('Вы зарегистрированы!')
#                 registration = True
#             else:
#                 print('Пароль должен быть 8 символов и не содержать спецсимволы!')
#         else:
#             print('Пароли должны совпадать!')
#     else:
#         print('Email должен содержать @ и заканчиваться на .ru или .com!')

# registration = False
#
# while not registration:
#     tel = input('Введите телефон в формате +79хххххххх: ')
#     name = input('Введите имя: ')
#     surname = input('Введите фамилию: ')
#     if tel.startswith('+79') and len(tel) == 12 and tel[1:].isdigit():
#         print(f'Ваше имя: {name.capitalize()}\n' f'Ваша фамилия: {surname.capitalize()}/n' f'Номер телефона: {tel}')
#         registration = True
#     else:
#         print('Невалидное имя фамилия')

# 1 задание
# string = input('Введите строку: ')
# print(string[::-1])

# 2 задание
# string = input('Введите строку: ')
# alpha = 0
# digit = 0
# for i in string:
#     if i.isalpha():
#         alpha += 1
#     elif i.isdigit():
#         digit += 1
# print(alpha, digit)


# 3 задание
# string = input('Введите строку: ')
# simbol = input('Введите искомый символ: ')
# print(string.count(simbol))

# 4 задание
# string = input('Введите строку: ')
# word = input('Введите искомое слово: ')
# print(string.count(word))

# 5 задание
# string = input('Введите строку: ')
# word = input('Введите искомое слово: ')
# repl_word = input('Введите заменяемое слово: ')
# print(string.replace(word, repl_word))

string_1 = input('Введите 1-Ю строку: ')
string_2 = input('Введите 2-Ю строку: ')
if string_2.lower() in string_1.lower():
    print('Есть контакт!')
else:
    print('Мимо!')