# def division(nam_1, nam_2):
#     # if nam_2 == 0:
#     #     return 'ошибка'
#     try:
#         return nam_1 / nam_2
#     except ZeroDivisionError:
#         return 'Деление на ноль'
#     finally:
#         print('Конец division')
#
#
# result = division(10 / 0)
# print(result)
# print('Блок кода после деления')

# def handler_exception(func):
#     def wrapper(*args, **kwargs):
#         try:
#             res = func(*args, **kwargs)
#             return res
#         except BaseException:
#             print(f'Возникла ошибка в {func.__name__} args{args} ')
#     return wrapper
#
# @handler_exception
# def division(nam_1, nam_2):
#     return nam_1 / nam_2
#
# @handler_exception
# def summa(num_1, num_2):
#     return num_1 + num_2
#
# res_1 = division(5, 2)
# res_2 = summa(5, '4')
# print(res_1)
# print(res_2)

import re

# sentence = 'hello world '
# res = re.match('hello', sentence)
# print(res.group())
text = "Andrey@gamil.com Andrey@gmail- com"
res = re.findall(r"\b\w{4,12}@\w{4,8}\.\w{2,3}\b", text)

print(res)
