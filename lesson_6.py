
# list_1 = [1, 2, 3, 4]
# list_2 = [5, 6, 7, 8]
# list_11 = ['1', '2', '3', '4']
# print(list_1 + list_2) # Объединее списков
# print(list_1 * 2) # Дублирование списков
# list_1.extend(list_2) # Расширение списка элеменами второго списка
# print(list_1)

# string = ' '
# # new_string = string.join(list_11)
# for i in list_1:
#     string += f'{i} '
# print(string)

# list comprehension

# list_1 = [i for i in range(1, 10)]
# for i in range(1, 10):
#     list_1.append(i)
# print(list_1)

# import sys
# list_1 = [i for i in range(1, 10)]
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sys.getsizeof(list_1))
# print(sys.getsizeof(list_2))

# list_1 = [i for i in range(1, 10) if i % 2 != 0]
# print(list_1)
# list_1 = [i ** 2 for i in range(1, 10) if i % 2 != 0]
# print(list_1)

# list_2 = [i for i in range(1, 5) for _ in range(5)]
# print(list_2)
# list_2 = [[i for i in range(1, 5)] for _ in range(5)]
# list_3 = [i * j for i in range(1, 5) for j in range(1, 5)]
# print(list_3)

# list_4 = [35, 7, 4, 87, 65]
# list_5 = [num for num in list_4 if num % 7 == 0]
# print(list_5)

# import string
# letters = string.ascii_letters
# input_text = 'hell@o m#y na!me is Ni$kita'
# letters_list = [letter for letter in input_text if letter in letters or letter.isspace()]
# print(''.join(letters_list))

# import string
# digits = string.digits
#
# input_text = 'qwqe7676 wqe787wqe qweqweq323'
# digits_list = [digit for digit in input_text if digit in digits]
# print(''.join(digits_list), len(digits_list))

# students = [['Петров', 4.5], ['Сидоров', 4.2], ['Иванов', 4.1], ['Иванова', 3.5], ['Петрова', 4.9]]
# students_2 = [student for student in students if student[1] >= 4.5]
# print(students_2)

