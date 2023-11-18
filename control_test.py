# Задача 1


# summ = 0
# while True:
#     number = int(input('Введите число: '))
#
#     summ += number
#     if number == 0:
#         break
# print(summ)

# Задача 2
# pass_true = 235
# while True:
#     password = int(input('Введите пароль: '))
#     if password != pass_true:
#         print('Пароль неверный! Попробуйте ещё раз:')
#     else:
#         print('Пароль верный! Добро пожаловать.')
#         break

# Задача 3
# money_sum = 0
# while True:
#     money = int(input('Сколько отложить денег? '))
#     money_sum += money
#     if money_sum >= 500000:
#         print(f'Вы накопили нужную сумму: {money_sum}')
#         break

# Задача 4
# number = int(input('Введите число: '))
# number_str = str(number)
# sum = 0
# for i in range(len(number_str)):
#     if number_str[i] == '5':
#         print('Обнаружен разрыв')
#         break
#     else:
#         number_int = int(number_str[i])
#         sum += number_int
# print(sum)

# Задача 5
# import time
# count = 10
# while True:
#     if count < 0:
#         print('Время вышло!')
#         break
#     else:
#         time.sleep(1)
#         print(count)
#         count -= 1

# Задача 6

# time = input('который час? Введите в формате ХХ.ХХ: ')
# hour = int(time[0:2])
# print('Ку-ку! ' * hour)

# Задача 7
# import time
# seconds = int(input('Введите количкство секунд: '))
# for i in range(seconds):
#     time.sleep(1)
#     seconds -= 1
#     print(seconds + 1)
# print('Я иду искать!')

# Задача 8
# text = input('Введите текст: ')
# simb_1 = 0
# simb_2 = 0
# for index in range(len(text)):
#     if text[index] == 'Ы':
#         simb_1 += 1
#     elif text[index] == 'ы':
#         simb_2 += 1
# print(f'Больших букв Ы: {simb_1}')
# print(f'Маленьких букв Ы: {simb_2}')

# Задача 9
# text = input('Введите текст: ')
# print(text.title())

# Задача 10
import random

while True:
    t = random.randint(1, 13)
    if t == 13:
        raise ValueError
    number = int(input("Введите число: "))
    if number < 666:
        print("Повторите ввод: ")
    else:
        print("Пока!")
        break

# Задача 11
# text = input('Введите текст: ')
# tx = []
# for i in range(len(text)):
#     if text[i] == 'h':
#         tx.append(i)
# tx_int = list(map(int, tx))
# print(text[tx_int[1]:tx_int[0]:-1][1:])
