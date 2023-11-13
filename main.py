# import module
# import math as m
# print(m.sin(30))
# from math import sin, cos, tan
# print(sin(30), cos(30), tan(30))
# from math import *
# print(factorial(5), pow(12, 2))

# def summa(a, b, c):
#     return a + b + c
#
# print(summa(10, 10, 14))

# def print(string):
#     return
#
# print('Hello')
# value_1 = 10
# def my_function():
#     global value_1 # вызов глобальной переменной
#     value_1 = 0
#     print(value_1)
#
# my_function()
# print(value_1)

# val_1 = 1
# def func_1():
#     val_2 = 2
#     def func_2():
#         nonlocal val_2 # вызов не локальной переменной
#         val_2 += 3
#         print(val_2)
#     print(val_2)
#     func_2()
# print(val_1)
# func_1()
#
# from math import *
# print(globals())

# def check_is_happy_num(number: str) -> bool:
#     """
#     Проверяет является ли число счастливым.
#     :param number: str
#     :return: bool
#     """
#     left = int(number[0]) + int(number[1]) + int(number[2])
#     right = int(number[3]) + int(number[4]) + int(number[5])
#     if left == right:
#         return True
#     return False
# print(check_is_happy_num('123420'))
# from typing import List
# def average_age(people: list[list]) -> float:
#     """
#     Функция среднего возроста
#     :param people: list
#     :return: flout
#     """
#     average: int = sum([i_human[1] for i_human in people])
#     return round(average / len(people), 1)
#
# people_list = [['Ivan', 35],['Petr', 27], ['Anna', 18],]
# print(average_age(people_list))

# def nechet_num(numbers_1, numbers_2: int) -> int:
#     """
#     Нечетные числа в диапозоне
#     :param numbers: int
#     :return: int
#     """
#
#
#     for i in range(numbers_1, numbers_2):
#         if i % 2 == 0:
#             print(i)
#
#
# nechet_num(2, 15)

def lines_simbol(numbers_1: int, numbers_2: bool, simbol: str):
    """
    Линия из символов
    :param numbers_1: int
    :param numbers_2: bool
    :param simbol: str
    :return: None
    """
    if numbers_2:
        print(simbol * numbers_1)
    else:
        for i in range(numbers_1):
            print(simbol)
lines_simbol(5, False, '*')
lines_simbol(5, True, '+')




