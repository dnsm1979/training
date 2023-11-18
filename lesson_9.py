# def function_1(a, b, *args):
#     print(a, b, args)
#
# function_1(1, 2, 3, 4, 5)

# def summa(*args): # Последовательность аргументов
#     # counter = 0
#     # for i_arg in args:
#     #     counter += i_arg
#     # return counter
#     return sum(args)
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8))

# def get_form(**kwargs): # именованый аргумент ( словарь )
#     print(kwargs['name'])
#
# get_form(name = 'Ivanov', email = 'ivanov@mail.ru')

# def get(reguest, *args, **kwargs):
#     print(f'Сделан запрос на {reguest}')
#     print(f'Параметр запроса {kwargs["cache_control"]}')
#     print(f'Относительный путь: {args[0]}')
#
# get('http://test.ru', '/rage_1', cache_control='no-cache', content_type='text/html')

# def group_stud(number, stepen, year, *args):
#     print(number, stepen, year)
#     counter = 0
#     for i in args:
#         counter += 1
#         print(counter, i)
#
#
#
# group_stud('A207', 'bakalavr', 2023, 'Ivanov', 'Petrov', 'Sidorov')
# def forma_valeu(value, data):
#     try:
#         print(data[value])
#     except KeyError:
#
#
#         print('Не заполнены обязательные формы!')
#         return
# def forma(**kwargs):
#     try:
#         print(kwargs['email'], kwargs['phone'])
#     except KeyError:
#
#
#         print('Не заполнены обязательные формы!')
#         return
#     # try:
#     #     print(kwargs['name'])
#     # except KeyError:
#     #     return
#     # try:
#     #     print(kwargs['surname'])
#     # except KeyError:
#     #     return
#     forma_value = ('name', kwargs)
#     forma_value = ('surname', kwargs)
#
# forma(email='mail@mail.ru', phone='899999999', name='Ivan', surname='Ivanov')

# square = lambda x, y: x ** y
#
# print(square(5, 3))

# num_list = [1, 2, 3, 4, 5, 6, 7, 8]
# square_num_list = [i ** 2 for i in num_list]
# print(square_num_list)
#
# square_num_list_2 = list(map(lambda x: x ** 2, num_list))
# print(next(square_num_list_2))
# print(next(square_num_list_2))
# print(next(square_num_list_2))
# import time
#
#
# class Interator:
#     def __init__(self, n):
#         self._n = n
#     def __iter__(self):
#         print('__iter__')
#         return self
#     def __next__(self):
#         print('__next__')
#         time.sleep(1)
#         self._n += 1
#         print(self._n)
#
#     for i in interator(0, 8, 2)

# num_list = [1, 2, 3, 4, 5, 6, 7, 8]
# square_num_list = [i ** 2 for i in num_list]
# print(square_num_list)
#
# filtered_list = list(filter(lambda x: x > 4, num_list))
# print(filtered_list)

# nums = [123, 14575, 35, 147, 489]
# filtered_num = list(filter(lambda x: x >= 100 and x <= 999, nums))
# print(filtered_num)
#
# filtered_num_1 = list(filter(lambda x: len(str(x)) == 3, nums))
# filtered_num_1 = list(map(int, filter(lambda x: len(str(x)) == 3, map(str(nums)))))

students = [
    ["Student 1", 4.8],
    ["Student 2", 4.7],
    ["Student 3", 4.9],
    ["Student 4", 4.6],
]

students_sorted = sorted(students, key=lambda x: x[1])
print(students_sorted)
