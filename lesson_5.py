# import sys
# my_list = ['Moskow', 'Samara', 'Novosibirsk', 'Ekaterinburg', 'Ekaterinburg', ]

# my_list2 = list(('Moskow', 'Samara', 'Novosibirsk', 'Ekaterinburg',))
# print(my_list)
# print(my_list)
# print(my_list2)
# print(sys.getsizeof(my_list))
# print(sys.getsizeof(my_list2))

# print(my_list[3])
# print(my_list[-3])
# print(my_list[1:])
# print(my_list[::2])
# print(my_list[::-1])
# my_list.append('Vladivostok') # Добовляет с конец списка
# my_list.append('Vladivostok')
# my_list.remove('Vladivostok') # Удаляет первое вхождение
# del_city = my_list.pop(2) # Удаляет элемент по индексу
# my_list.insert(0, 'Chelyabinsk') # Вставляет элемент по указанному индексу
# print(my_list.count('Ekaterinburg')) # Возвращает количество конктетного элемента
# print(my_list.index('Ekaterinburg')) # Возвращает индекс элемента
# my_list[3] = 'Vladivostok' # Присваивание элемента
# my_list.reverse()
# print(my_list)

# my_list = ['Moskow', 'Samara', 'Novosibirsk', 'Ekaterinburg',  ]

# for i_city in my_list:
#     print(f'Город: {i_city}')

# for index in range(len(my_list)):
#     print(f'{index + 1} Город: {my_list[index]}')

# num_d1 = int(input('Введите первое число диапозона: '))
# num_d2 = int(input('Введите второе число диапозона: '))
# list_d = []
# for i in range(num_d1, num_d2 + 1):
#     if i % 2 != 0:
#         list_d.append(i)
# print(list_d)

# basket_1 = ['Bayern', 'Man Utd', 'Juventus', 'Barselona']
# basket_2 = ['Real Madrid', 'Man Sity', 'Milan', 'Porto']
# for index in range(len(basket_1)):
#     if index % 2 != 0:
#         print(f'{basket_1[index]} - {basket_2[index - 1]}')
#         print(f'{basket_1[index - 1]} - {basket_2[index]}')

# numbers = [15, 4, 8, 17, 79, 5, 1, 4]
# numbers.sort(reverse=True)
# numbers_sorted = sorted(numbers)
# print(numbers, numbers_sorted)

# letters = ['a', 'z', 'b', 'r', ]
# print(sorted(letters))

# string = 'hello python java ruby'
# print(string.split())

# numbers = input('Введите числа через пробел: ').split()
# for i_num in numbers:
#     numbers[numbers.index(i_num)] = int(i_num) # Преобразование строк в числа из списка

# for index, value in enumerate(numbers):
#     numbers[index] = int(value)  # Преобразование строк в числа из списка

# numbers_int = list(map(int, numbers))
# print(numbers_int)   # Преобразование строк в числа из списка

# films = ['Побег из шоушенко', 'Зеленая миля', 'Поймай меня если сможешь', 'Волк с Уолт-Стрит', ]
# liked_films = []
#
# while True:
#     choice = input('1-Посмотреть список фильмов\n'
#                    '2-Добавить фильм в избранное\n'
#                    '3-Удалить из избранного - > ')
#     if choice == '1':
#         print(f'Ваш список фильмов: ', *liked_films)
#     elif choice == '2':
#         film = input('Введите название фильма: ')
#         if film in films:
#             if film not in liked_films:
#                 liked_films.append(film)
#                 print('Ваш фильм добавлен!')
#             else:
#                 print('Такой фильм у вас уже есть!')
#         else:
#             print('Такого фильма в нашей библиотеке нет, добавим его позже...')
#     elif choice == '3':
#         film = input('Введите название фильма: ')
#         if film in liked_films:
#             liked_films.remove(film)
#             print('Фильм удален из избранного!')
#         else:
#             print('Такого фильма у вас нет!')
#     else:
#         print('До новых встреч!')
#         break

# numbers = [1, 25, 78, 7, 4, -9]
# print(numbers)
# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))

# numbers = input('Введите числа через пробел: ').split()
# num_count = input('Введите число: ')
# print(numbers.count(num_count))
numbers = input("Введите числа через пробел: ").split()
num_count = int(input("Введите число: "))
numbers_int = list(map(int, numbers))
t = 0
for i in range(len(numbers_int)):
    if num_count == numbers_int[i]:
        t += 1
print(t)

# numbers = input('Введите числа через пробел: ').split()
# numbers_int = list(map(int, numbers))
# sr_oriph = 0
# sr_oriph2 = 0
# for index in numbers_int:
#     sr_oriph += index
# print(f'Сумма всех чисел списка: {sr_oriph}')
# for index2 in numbers_int:
#     sr_oriph2 += index2
# print(f'Среднеарифметическое равно: {sr_oriph2 / len(numbers_int)}')
