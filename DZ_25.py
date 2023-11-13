# 1 - Задание
# import json
#
# def add_new_country():
#     country = input('Введите название страны: ')
#     city = input('Введите название столицы: ')
#     return add_new_country_to_file(country, city)
#
#
# def add_new_country_to_file(country, city):
#     with open ('Countris.json', 'r') as file:
#         country_dict = json.loads(file.read())
#         keys_dict = country in country_dict
#         if keys_dict == False:
#             country_dict[country] = city
#             print(f'Данные добавлены!')
#         else:
#             print(f'Страна {country} уже есть в словаре!')
#     with open('Countris.json', 'w') as file:
#         file.write(json.dumps(country_dict))
#
# def del_country_in_file(country):
#     with open('Countris.json', 'r') as file:
#         country_dict = json.loads(file.read())
#         keys_dict = country in country_dict
#         if keys_dict == True:
#             del country_dict[country]
#             print(f'{country} удален из словаря!')
#         else:
#             print(f'{country} нет в словаре!')
#     with open('Countris.json', 'w') as file:
#         file.write(json.dumps(country_dict))
#
# def search_country_in_file(search):
#     with open ('Countris.json', 'r') as file:
#         country_dict = json.loads(file.read())
#         for k, v in country_dict.items():
#             if k == search or v == search:
#                 print(f'{search} есть в словаре! {k}: {country_dict[k]}')
#                 break
#
#         else:
#             print(f'{search} нет в словаре!')
#         # keys_dict = country in country_dict
#         # if keys_dict == True:
#         #     print(f'{country} есть в словаре!')
#         # else:
#         #     print(f'{country} нет в словаре!')
#
# def edit_key_dict_country(country, new_country):
#     with open('Countris.json', 'r') as file:
#         country_dict = json.loads(file.read())
#         keys_dict = country in country_dict
#         if keys_dict == True:
#             country_dict[new_country] = country_dict[country]
#             del country_dict[country]
#             print(f'{country} заменен на {new_country} в словаре!')
#
#         else:
#             print(f'{country} нет в словаре!')
#     with open('Countris.json', 'w') as file:
#         file.write(json.dumps(country_dict))
#
# def edit_value_dict_country(city, new_city):
#     with open('Countris.json', 'r') as file:
#         country_dict = json.loads(file.read())
#         for k, v in country_dict.items():
#             if v == city:
#                 country_dict[k] = new_city
#                 print(f'{city} заменен на {new_city} в словаре!')
#                 break
#         else:
#             print(f'{city} нет в словаре!')
#
#     with open('Countris.json', 'w') as file:
#         file.write(json.dumps(country_dict))
#
# def get_dict_country():
#     with open('Countris.json', 'r') as file:
#         country_dict = json.loads(file.read())
#         print(country_dict)
#
# while True:
#     choice = int(input(f'1-Добавление страны и столицы в словарь\n'
#                    f'2-Удаление страны и столицы из словаря\n'
#                    f'3-Поиск данных\n'
#                    f'4-Редактирование страны\n'
#                    f'5-Редактирование столицы\n'
#                    f'6-Показать словарь   ->'))
#     if choice == 1:
#         add_new_country()
#     elif choice == 2:
#         del_country_in_file(input('Какую страну удалить из словаря? '))
#     elif choice == 3:
#         search_country_in_file(input('Введите ключевое слово для поиска: '))
#     elif choice == 4:
#         edit_key_dict_country(input('Редактируемое название страны: '), input('Новое название: '))
#     elif choice == 5:
#         edit_value_dict_country(input('Редактируемое название столицы: '), input('Новое название: '))
#     elif choice == 6:
#         get_dict_country()
#
#     else:
#         print('Такого пункта нет!')

# add_new_country()
# search_country_in_file('Russ')
# del_country_in_file('Italy')
# edit_key_dict_country('Russia', 'Russ')
# edit_value_dict_country('Mow', 'Moscow')
# get_dict_country()


# 2 - Задание
import json

def add_new_performer():
    performer = input('Введите название исполнителя: ')
    album = input('Введите название альбома: ')
    return add_new_performer_to_file(performer, album)


def add_new_performer_to_file(performer, album):
    with open ('Performers.json', 'r') as file:
        performer_dict = json.loads(file.read())
        keys_dict = performer in performer_dict
        if keys_dict == False:
            performer_dict[performer] = album
            print(f'Данные добавлены!')
        else:
            print(f'Исполнитель {performer} уже есть в словаре!')
    with open('Performers.json', 'w') as file:
        file.write(json.dumps(performer_dict))

def del_performer_in_file(performer):
    with open('Performers.json', 'r') as file:
        performer_dict = json.loads(file.read())
        keys_dict = performer in performer_dict
        if keys_dict == True:
            del performer_dict[performer]
            print(f'{performer} удален из словаря!')
        else:
            print(f'{performer} нет в словаре!')
    with open('Performers.json', 'w') as file:
        file.write(json.dumps(performer_dict))

def search_performer_in_file(search):
    with open ('Performers.json', 'r') as file:
        performer_dict = json.loads(file.read())
        for k, v in performer_dict.items():
            if k == search or v == search:
                print(f'{search} есть в словаре! {k}: {performer_dict[k]}')
                break

        else:
            print(f'{search} нет в словаре!')


def edit_key_dict_performer(performer, new_performer):
    with open('Performers.json', 'r') as file:
        performer_dict = json.loads(file.read())
        keys_dict = performer in performer_dict
        if keys_dict == True:
            performer_dict[new_performer] = performer_dict[performer]
            del performer_dict[performer]
            print(f'{performer} заменен на {new_performer} в словаре!')

        else:
            print(f'{performer} нет в словаре!')
    with open('Performers.json', 'w') as file:
        file.write(json.dumps(performer_dict))

def edit_value_dict_performer(album, new_album):
    with open('Performers.json', 'r') as file:
        performer_dict = json.loads(file.read())
        for k, v in performer_dict.items():
            if v == album:
                performer_dict[k] = new_album
                print(f'{album} заменен на {new_album} в словаре!')
                break
        else:
            print(f'{album} нет в словаре!')

    with open('Performers.json', 'w') as file:
        file.write(json.dumps(performer_dict))

def get_dict_performer():
    with open('Performers.json', 'r') as file:
        performer_dict = json.loads(file.read())
        print(performer_dict)

while True:
    choice = int(input(f'1-Добавление исполнителя и альбома в словарь\n'
                   f'2-Удаление исполнителя и альбома из словаря\n'
                   f'3-Поиск данных\n'
                   f'4-Редактирование исполнителя\n'
                   f'5-Редактирование название альбома\n'
                   f'6-Показать словарь   ->'))
    if choice == 1:
        add_new_performer()
    elif choice == 2:
        del_performer_in_file(input('Какого исполнителя удалить из словаря? '))
    elif choice == 3:
        search_performer_in_file(input('Введите ключевое слово для поиска: '))
    elif choice == 4:
        edit_key_dict_performer(input('Редактируемое название исполнителя: '), input('Новое название: '))
    elif choice == 5:
        edit_value_dict_performer(input('Редактируемое название альбома: '), input('Новое название: '))
    elif choice == 6:
        get_dict_performer()

    else:
        print('Такого пункта нет!')