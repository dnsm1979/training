# 1 Задание
# import random
#
#
# def trying(func):
#     def wrapper(*args, **kwargs):
#         if 10 == random.randint(1, 10):
#             raise ValueError
#         else:
#             print(f'{int(func(*args, **kwargs))}')
#     return wrapper
# @trying
# def func_dr(a, b):
#     return a / b
#
# func_dr(6, 3)

# 2 Задание
def Type_func(func):
    def wrapper(*args, **kwargs):
        print(f'Функция вернула значение:{type(func(*args, **kwargs))}')
        if type(func(*args, **kwargs)) is int:
            print('Число')
        elif type(func(*args, **kwargs)) is str:
            print('Строка')
        elif type(func(*args, **kwargs)) is dict:
            print('Словарь')
        elif type(func(*args, **kwargs)) is list:
            print('Список')
        elif type(func(*args, **kwargs)) is set:
            print('Множество')

    return wrapper


@Type_func
def func_Type(a):
    return a

func_Type({8, 't'})
