import sys

# dictionary = {'name': 'Ivan', 'age': 32}
# # print(dictionary)
# # print(type(dictionary))
# import sys
# name = dictionary.get('name')
# dictionary['age'] = 33 # Установка нового значения
# dictionary['surname'] = 'Ivanov'
# dictionary.pop('age') # удаляет значение по ключу
# list_man = ['Ivan', 32, 'ivanov']
# print(sys.getsizeof(dictionary))
# print(sys.getsizeof(list_man))


# print(dictionary.keys()) # Показывает ключи
# print(dictionary.values())# Показывает значения
# print(dictionary.items())# Показывает ключ и значения

# dictionary_2 = {'name': 'Petya', 'age': 32}
# dictionary.update(dictionary_2) # Заменяет значения в словаре
# dictionary.setdefault('adress', '') # Устанавливает ключ по кмолчанию
#
#
# print(dictionary)
#
# didtionary = {}
# def set_country(country):
#     didtionary.setdefault(country, [])
#     print('Страна добавлена')
#
# def set_sity():
#     key = (input('Страна: '))
#     country = didtionary.get(key)
#     city_name = input('Введите название города: ')
#     if country or country == []:
#         for i_city in country:
#             if city_name in i_city.keys():
#                 print('Такой город уже есть!')
#                 return
#         population = int(input('введите население города: '))
#         time_zone = input('Часовой пояс: ')
#         new_city = {city_name: {'population': population, 'time_zone': time_zone}}
#         didtionary[key].append(new_city)
#         print('Город добавлен!')
#     else:
#         print('Такой страны нет!')
#
# def get_city_info():
#     country = input('Страна: ')
#     get_country = didtionary.get(country)
#     if get_country:
#         city = input('Введите название города: ')
#         for i_city in get_country:
#             if city in i_city.keys():
#                 city_info = i_city[city]
#                 print(f'Население города: {city_info.get("population")}\n'f'Часовой пояс: {city_info.get("time_zone")}')
#                 return
#     else:
#         print('Такой страны нет!')
#
#
#
#
# def main():
#     while True:
#         choice = input('1-Добавить страну\n''2-Добавить город\n''3-Добавить инфо по городу ->')
#         if choice == '1':
#             country = input('Введите название страны: ')
#             set_country(country)
#         elif choice == '2':
#             set_sity()
#         elif choice == '3':
#             get_city_info()
#
# main()

# text = input('Введите текст: ')
# frequency_dict = {}
#
# for i_symbol in text:
#     if not i_symbol.isspace():
#         frequency_dict.setdefault(i_symbol, 0)
#         frequency_dict[i_symbol] += 1
# print(frequency_dict)
# for key, value in frequency_dict.items():
#     print(f'{key}: {value}')

# text = input('Введите текст: ')
# frequency_dict = {}
#
# for i_symbol in text:
#     if not i_symbol.isspace():
#         if i_symbol  in frequency_dict.keys():
#             frequency_dict[i_symbol] += 1
#         else:
#             frequency_dict[i_symbol] = 1
# print(frequency_dict)
# for key, value in frequency_dict.items():
#     print(f'{key}: {value}')

# text = input('Введите текст: ')
# frequency_dict = {}
#
# for i_symbol in text:
#     if not i_symbol.isspace():
#         count = text.count(i_symbol)
#         if count in frequency_dict.keys():
#             if i_symbol not in frequency_dict[count]:
#                 frequency_dict[count].append(i_symbol)
#             else:
#                 frequency_dict[count] = [i_symbol]
#
#
#
# print(frequency_dict)
# for key, value in frequency_dict.items():
#     print(f'{key}: {value}')

dict_1 = {"key_1": {"key_2"}}
