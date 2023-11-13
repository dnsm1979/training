
# age = int(input('Введите ваш возрост: '))
# if 18 >= age >= 70:
#     print('Вы можете зарегистрироваться! ')
# else:
#     print('Вам нельзя зарегистрироваться!')

# weekday = int(input('Введите номер дня недели: '))
# if weekday == 1:
#     print('Понедельник')
# elif weekday == 2:
#     print('Вторник')
# elif weekday == 3:
#     print('Среда')
# elif weekday == 4:
#     print('Четверг')
# elif weekday == 5:
#     print('Пятница')
# elif weekday == 6:
#     print('Суббота')
# elif weekday == 7:
#     print('Воскресенье')
# else:
#     print('Нет такого!')


# email = 'nikita@mail.ru'
# password = '12345nik'
# email_input = input(' Введите email: ')
# password_input = input('Введите пароль: ')
# # authorization = False
# if email_input == email:
#     if password_input == password:
#         # authorization = True
#         print('Вы авторизовались')
#     else:
#         print('Пароль не верный!')
# else:
#     print('email не верный!')

# match(authorization):
#     case True:
#         print('Пользователь успешно автороризовался!')
#     case False:
#         print('Пользователь не автороризовался!')
#
# number = int(input('Введите число: '))
# # if number % 2 != 0:
# #     print('нечетное')
# # else:
# #     print('Четное')
#
#
# if number % 6 == 0:
#     print('Число кратно 6')
# else:
#     print('Число не кратно 6')
# from math import sqrt
# import math
# print('a*x^2 + c')
# a = float(input('Введите коэффицент a: '))
# b = float(input('Введите коэффицент b: '))
# c = float(input('Введите коэффицент c: '))
# D = b**2 - 4 * a * c
# if D < 0:
#     print('Корней нет!')
# elif D == 0:
#     x = -b / (2 * a)
#     print(f'x = {x}')
# else:
#     x1 = (-b + sqrt(D)) / (2 * a)
#     x2 = (-b - sqrt(D)) / (2 * a)
#     print(f'x1={round(x1, 2)} x2={round(x1, x2)}')

# number_1 = int(input('1-ое число: '))
# number_2 = int(input('2-ое число: '))
# # if number_2 == 0:
#     print('На ноль делить нельзя!')
# else:
#     print(number_1 / number_2)

#
# try:
#     print(number_1 / number_2)
# # except ZeroDivisionError:
# #     print('На ноль делить нельзя!')
# # else:
# #     print('Программа выполнена без ошибок!')

# try:
#     raise ValueError('Вызвана ошибка специально')
# except FileExistsError:
#     print('Обработана ошибка')

# try:
#     raise ValueError('Вызвана ошибка специально')
# except KeyError:
#     print('Обработчик ошибок 1')
# except ValueError:
#     print('Обработчик ошибок 2')
# try:
#     year = int(input('Введите год: '))
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print('Год високосный')
#     else:
#         print('Год не  високлсный')
# except (ValueError, TypeError):
#     print('Год должен быть числом!')
# try:
#     number = int(input('Введите число: '))
#
#     if number % 7 == 0:
#         print('Число кратное 7')
#     else:
#         print('Число не кратное 7')
# except ValueError:
#     print('Нужно ввести число!')

# try:
#     number_1 = int(input('Введите 1 число: '))
#     number_2 = int(input('Введите 2 число: '))
#
#     if number_1 > number_2:
#         print(number_1)
#     elif number_2 > number_1:
#         print(number_2)
#     else:
#         print('Числа ровны!')
# except ValueError:
#     print('Нужно ввести число!')

# try:
#     number_1 = int(input('Введите 1 число: '))
#     number_2 = int(input('Введите 2 число: '))
#
#     if number_1 < number_2:
#         print(number_1)
#     elif number_2 < number_1:
#         print(number_2)
#     else:
#         print('Числа ровны!')
# except ValueError:
#     print('Нужно ввести число!')
# try:
#     number_1 = int(input('Введите 1 число: '))
#     number_2 = int(input('Введите 2 число: '))
#     v = int(input('Выберите действие: 1 - сумма, 2 - разность, 3 - среднеорифметическое, 4 - произведение: '))
#
#     if 1 > v or v > 4:
#         print('Выбран не существующий пункт!')
#     else:
#         if v == 1:
#             print(number_1 + number_2)
#         elif v == 2:
#             print(number_1 - number_2)
#         elif v == 3:
#             print((number_1 + number_2) / 2)
#         else:
#             print(number_1 * number_2)
# except ValueError:
#     print('Нужно ввести число!')
# try:
#     second = int(input('Введите количество секунт, прошедшие с начала дня: '))
#     v = int(input('Выберите фотмат отображения: 1 - в часах, 2 - в минутах, 3 - секундах : '))
#     if 1 > v or v > 3:
#         print('Выбран не существующий пункт!')
#     else:
#         second_end = 43200 - second
#         if v == 1:
#             print(round((second_end / 60 / 60) , 2))
#         elif v == 2:
#             print(round(second_end / 60, 2))
#         else:
#             print(second_end)
#
#
#
# except ValueError:
#     print('Нужно ввести число!')

# except ValueError:
#     print('Нужно ввести число!')
# try:
# hours = int(input('Введите текущий час: '))
#
# if 1 > hours or hours > 23:
#     print('Выбран не существующий час!')
# else:
#     if 6 < hours or hours > 11:
#         print('Пора вставать!')
#     else:
#         print('Ты проспал!')

# ocenka_1 = int(input('Введите оценку 1: '))
# ocenka_2 = int(input('Введите оценку 2: '))
# ocenka_3 = int(input('Введите оценку 3: '))
#
# sum_ocenka = ocenka_1 + ocenka_2 + ocenka_3
# if 250 <= sum_ocenka:
#     print('Сумма балов: ', sum_ocenka, 'Ты поступил неа бюджет!')
# else:
#     print('Сумма балов: ', sum_ocenka, 'Ты не поступил на бюджет!')

minut = int(input('Введите количество минут: '))
hours = minut // 60
ost_min = minut % 60
print(hours, ost_min)


