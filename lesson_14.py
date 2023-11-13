import datetime
import functools
from typing import Callable
import time
# def timer(func:Callable, *args, **kwargs):
#     print('Запускается таймер')
#     start = time.time()
#     res = func()
#     print(f'Функция выполнялась {time.time() - start}')
#     return res
# def timer(func: Callable) -> Callable:
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs): # Функция обертка
#         start = time.time()  #  код для допю функционала
#         func(*args, **kwargs)   #  вызов функции
#         print(f'Функция {func.__name__}{func.__doc__} выполнялась за {time.time() - start}') # код для допю функционала

#     return wrapper #  возвращаем функцию обертку
# @timer
# def squares_sum(num):
#     """
#       Квадраты чисел
#       :param func:
#       :return:
#       """
#     nums = [i ** 2 for i in range(num)]
#     return nums
# @timer
# def cubes_sum():
#     nums = [i ** 3 for i in range(1000000)]
#     return nums
#
# squares_sum(100000)
# cubes_sum()

# def get_or_post(metod):
#     def wrapper_func(func):
#         def wrapper():
#             if metod == 'GET':
#                 res = func()
#                 print(f'Запрос с методом {metod} на ресурс {res} выполнен')
#         return wrapper
#     return wrapper_func
#
# @get_or_post('GET')
# def request():
#     url = 'http://test.com'
#     params = 'ru'
#     request_body = {}
#     return url, params, request_body
#
# request()
# def beuty_output(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         for i in result:
#             print(f'|{i}|')
#     return wrapper
#
#
# @beuty_output
# def names_output(names):
#     return names
#
# names_output(['Nikita', 'Ivan', 'Maria'])

# def logging(func: Callable) -> Callable:
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#             print(f'{func.__name__} {func.__doc__}')
#         except BaseException as error:
#             with open('function_error.log', 'a') as file:
#                 file.write(f'{func.__name__} {datetime.datetime.now()} | {error.__doc__}\n ')
#     return wrapper
#
#
# def timer(func: Callable) -> Callable:
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs): # Функция обертка
#         start = time.time()  #  код для допю функционала
#         func(*args, **kwargs)   #  вызов функции
#         print(f'Функция {func.__name__}{func.__doc__} выполнялась за {time.time() - start}') # код для допю функционала
#     return wrapper
# @timer
# @logging
# def concatenate(a, b):
#     return a + b
# @timer
# @logging
# def devision(a, b):
#     return  a / b
#
# concatenate(1, 'a')
# devision(5, 0)

# def double(x):
#     def wrapt(func):
#         def wrapper(*args, **kwargs):
#             print(f'{int(func(*args, **kwargs))}\n' * x)
#         return wrapper
#     return wrapt
#
# @double(4)
# def func_dr(a, b):
#     return a / b
#
# func_dr(6, 3)



# import time
# def sleep(func:Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         time.sleep(9)
#         print(f'{int(func(*args, **kwargs))}')
#     return wrapper
#
#
# @sleep

# def proverka(func:Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         age = int(input('Введите возрост: '))
#         if age < 18:
#             print('Доступ закрыт!')
#         else:
#             print(f'{int(func(*args, **kwargs))}')
#     return wrapper
#
# @proverka
# logs = {}
# def logger_dict(func:Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         print(f'{int(func(*args, **kwargs))}')
#         logs = (func.__name__, func.__doc__)
#         print(logs)
#     return wrapper
#
#
#
# @logger_dict
# def func_dr(a, b):
#     return a / b
#
# func_dr(6, 3)




def nums(*args, **kwargs):






