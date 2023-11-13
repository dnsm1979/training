# Множества

# a = set() # Соэдание множества
# a.add('apple') # Добовление элементов в множество
# a.add('banana')
# a.remove('apple') # Удаляет элемент
# a.discard('appl') # Удаляет элемент с исключением
# a.pop() # Удаляет любой элемент


# print(a)
# print('banana' in a)
# b = {'orange', 'watermelon', 'apple'}
# print(a.intersection(b)) # пересечение множеств
# print(b.difference(a))  # разница множеств
# print(a.union(b)) # Объединение множеств
# print(a.clear()) # Отчистка
# a.update(b) # обновление множества
# print(a)
# for item in a:
#     print(item)
# print(*a) # через пробел
# print('*'.join(a)) # через заданный символ
# set_1 = {'name', 18, 'key', 'value'}
# print(*set_1)
# import sys
# list_1 = ['apple', 'orange']
# set_1 = {'apple', 'orange'}
# print(sys.getsizeof(list_1))
# print(sys.getsizeof(set_1))
# print(set_1.update(list_1))

# with open('text.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     set_1 = set(text)
#     print(len(set_1))
# data = {}
# with open('WW.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     symbols = set(text)
#     file.seek(0)
#     for symbol in symbols:
#         if symbol.isalpha():
#             data[symbol] = text.count(symbol)
#     sorted_dict = sorted(data, key=lambda x: data[x], reverse=True)
#     print(data['о'])
# print(sorted_dict)
# pl_dict = {}
# str_1 = input('Введите строку: ')
# x = len(str_1)
# if x % 2 == 0:
#     for i in str_1:
#         pl_dict[i] = str_1.count(i)
#     print(pl_dict.values())
#     for j in pl_dict.values():
#         if int(j) % 2 == 0:
#             print(True)
#         else:
#             print(False)


# string = 'abbcvvccbba' # Проверка строки на полиндром
#
# def check(sting):
#     data = {}
#     for i in string:
#         data.setdefault(i, 0)
#         data[i] += 1
#
#     count = 0
#     for j in data.values():
#         if j  % 2 != 0:
#             count += 1
#     if  count <= 1:
#         print('Может')
#     else:
#         print('Не может')
#
# check(string)

# Генераторы
# import sys
# list_1 = [i for i in range(100)]
# generation = (i for i in range(100)) # генераторное вырожение
# for i in generation:
#     print(i)
#
# print(sys.getsizeof(list_1))
# print(sys.getsizeof(generation))
# def custom_range(start, end):
#     for i in range(start, end):
#         yield i
#
#
# for i in custom_range(10, 20):
#     print(i)

# class genetation:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.cur = start
#
#     def __iter__(self):
#         print('__iter__')
#         return self
#
#     def __next__(self):
#         print('__next__')
#         if  self.cur == self.end:
#             raise StopIteration
#         self.cur += 1
#         return self.cur
#
# for i in genetation(10, 20):
#     print(i)
# import sys
# list_1 = [i for i in range(100)]
# generation = (i for i in range(100))
# print(generation.__next__())
# print(generation.__next__())
# print(generation.__next__())
# print(generation.__next__())
# print(generation.__next__())
# print(generation.__next__())
# print(generation.__next__())
# print(generation.__next__())
# print(generation.__next__())

# with open('text_2.txt', 'r') as file:
#     words = set((i_word for i_word in file.readlines()))
#     print(words)
# for i in words:
#     print(i.strip())

# def words():
#     with open('text_2.txt', 'r') as file:
#         for i in file.readlines():
#             yield i
#
# for i in words():
#     print(i.strip())
# num = 0
# def endless():
#     while num:
#
#         num += 1
#         yield num
#
# for i in endless():
#     print(i)

names = ['Anna', 'Ivan', 'Oleg']
gen = (i for i in names if 'a' not in i)
print(*gen)
