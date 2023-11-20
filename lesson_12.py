# turple_1 = ('Ivan', 15)
# turple_2 = (turple_1 + ('Petr', 15))
# # print(turple_1 + ('Petr', 15))
#
# # print(turple_2 * 2)
# # turple_2[0][0] ='Maria'
# print(turple_2.count(15))
# print(turple_2.index(15))
# import sys
# turple_1 = ('Ivan', 25) # O(n)
# list_1 = ['Ivan', 25]   # O(n)
# dict_1 = {'Ivan': 25}   # O(1)
# print(sys.getsizeof(turple_1))
# print(sys.getsizeof(list_1))
# print(sys.getsizeof(dict_1))

# dict_1 = {('Ivan', 'Ivanov'): 25}
# print(dict_1[('Ivan', 'Ivanov')])

# list_1 = ['Ivan', 'Ivanov']
# print(tuple(list_1))
# list_1 = ('Ivan', 'Ivanov')
# print(list(list_1))

# a = 10, 20
# print(a)

# zip
#
# list_1 = ['Moscow', 'Berlin']
# list_2 = [1000000, 2000000, 300000]
# print(dict(zip(list_1, list_2)))

# list_1 = ('Moscow', 'Berlin')
# list_2 = (1000000, 2000000, 300000)
# print(dict(zip(list_1, list_2)))

# list_1 = ['Moscow', 'Berlin']
# list_2 = (1000000, 2000000, 300000)
# print(list(zip(list_1, list_2)))

# dictionary = {}
# import re
# def add_competition() -> None:
#     competition = input('Название соревнования: ')
#     date = input('Дата проведения yyyy/mm/dd HH:MM')
#     if  re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}', date) and (competition, date) not in dictionary.keys():
#         dictionary.update({(competition, date): []})
#         print('Соревнование добавлено!')
#         return
#     print('Невалидный ввод!')
#
# def add_members() -> None:
#     competition = input('Название соревнования: ')
#     date = input('Дата проведения yyyy/mm/dd HH:MM')
#     if re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}', date) and (competition, date) in dictionary.keys():
#         choice = input('1-Добавить участников или убрать?  add/del')
#         members = dictionary[(competition, date)]
#         if choice == 'add':
#             input_members = input('Введите участников через ,: ').split(', ')
#             dictionary[(competition, date)] = members + input_members
#             print('Участники добавлены!')
#         elif choice == 'del':
#             del_members = input('Введите участников через ,: ').split(', ')
#             for i_members in del_members:
#                 members.remove(i_members)
#             dictionary[(competition, date)] = members
#             print('Участники удалены!')
#             return
#
#     else:
#         print('Ошибка ввода!')
#
#
# def info() -> None:
#     competition = input('Название соревнования: ')
#     date = input('Дата проведения yyyy/mm/dd HH:MM')
#     if re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}', date) and (competition, date) in dictionary.keys():
#         print(f'{competition} {date}')
#         for index, i_members in enumerate(dictionary[(competition, date)]):
#             print(f'{index + 1} {i_members}')
#         return
#     else:
#         print('Ошибка ввода!')
#
#
# def main() -> None:
#     while True:
#         choice = input('1-Добавить соревнования\n'
#                        '2-Вности участников соревнования\n'
#                        '3-Вывод данных по конкретному соревнованию: ')
#         if choice == '1':
#             add_competition()
#         elif choice == '2':
#             add_members()
#         elif choice == '3':
#             info()
#
# main()

# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#
# def ceasar_code(text, shift) -> str:
#     decrypted_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in text.lower()]
#     return ''.join(decrypted_list)
#
#
# text = input('Введите текст: ')
# shift = int(input('Введите сдвиг: '))
# print(ceasar_code(text, shift))
#
# ceasar_code()

# site = {
#     'body':{
#         'div':{
#             'ul':{
#                 'li_1':{},
#                 'li_2':{
#                     'href': 'какая то ссылка'
#                 }
#             }
#         }
#     }
# }
#
# # print(site['body']['div']['ul']['li_2']['href'])
#
# def get(key, dictiory, levil=0):
#     if key in dictiory.keys():
#         print(dictiory[key])
#         print(levil)
#         return
#     for value in dictiory.keys():
#         if isinstance(dictiory[value], dict):
#
#             get(key, dictiory[value], levil + 1)
#
# print(get('href', site))

text = ("banana", "apple", "bananamango", "mango", "srtawberry-banana")
fruct = input("Введите фрукт для поиска")
t = 0
for i in text:
    if fruct in text[i]:
        t += 1
print(t)
