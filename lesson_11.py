# import  re
# data = {}
# def add_money() -> None:
#     date = input('(уууу/мм)-> ')
#     if re.match(r'\d{4}/\d{2}', date):
#         money = float(input(f'Ваша прибыль за {date}: '))
#         year, month = date.split('/')
#         data.setdefault(year, {})
#         data[year].setdefault(month, 0)
#         data[year][month] += money
#         # print(data)
#     else:
#         print('Формат даты не верный!')
#
# def get_year_cost() -> None:
#     year = input('Введите год: ')
#     if re.match(r'\d{4}', year) and year in data.keys():
#         print(f'Ваша прибыль за {year} ровна {sum(data[year].values())}')
#     else:
#         print('Такого года нет!')
#
#
# def get_month_cost() -> None:
#     date = input('yyyy/mm->')
#     if re.match(r'\d{4}/\d{2}', date):
#         year, month = date.split('/')
#         if year in data.keys():
#             if month in data[year].keys():
#                 print(f'Ваша прибыль за {date} составила: {data[year][month]}')
#             else:
#                 print('Такого месяца нет!')
#         else:
#             print('Такого года нет!')
#     else:
#         print('Не верный формат даты!')
#
#
# def main() -> None:
#     while True:
#         choice = input('1-Внести прибыль за периуд в формате уууу/мм\n'
#                        '2-Получить прибыль за конкретный месяц (уууу/мм)\n'
#                        '3-Получить прибыль за конкретный год (уууу):')
#         if choice == '1':
#             add_money()
#         elif choice == '2':
#             get_month_cost()
#         elif choice == '3':
#             get_year_cost()
#         else:
#             print('Такой команды нет!')
#
#
# main()

# import  re
# data = {}
# def add_money() -> None:
#     date = input('(уууу/мм)-> ')
#     if re.match(r'\d{4}/\d{2}', date):
#         money = float(input(f'Ваша прибыль за {date}: '))
#         year, month = date.split('/')
#         data.setdefault(year, 0)
#         data.setdefault(date, 0)
#         data[date] += money
#         data[year] += money
#         # print(data)
#     else:
#         print('Формат даты не верный!')
#
# def get_year_cost() -> None:
#     year = input('Введите год: ')
#     if re.match(r'\d{4}', year) and year in data.keys():
#         print(f'Ваша прибыль за {year} ровна {data[year]}')
#     else:
#         print('Такого года нет!')
#
#
# def get_month_cost() -> None:
#     date = input('yyyy/mm->')
#     if re.match(r'\d{4}/\d{2}', date):
#         if date in data.keys():
#
#             print(f'Ваша прибыль за {date} составила: {data[date]}')
#         else:
#                 print('Такого месяца нет!')
#
#     else:
#         print('Не верный формат даты!')
#
#
# def main() -> None:
#     while True:
#         choice = input('1-Внести прибыль за периуд в формате уууу/мм\n'
#                        '2-Получить прибыль за конкретный месяц (уууу/мм)\n'
#                        '3-Получить прибыль за конкретный год (уууу):')
#         if choice == '1':
#             add_money()
#         elif choice == '2':
#             get_month_cost()
#         elif choice == '3':
#             get_year_cost()
#         else:
#             print('Такой команды нет!')
#
#
# main()
#
# contacts_ls = {}
# import re
# def add_contact() -> None:
#     contact = input('Введите данные контакта (Name,Phone)')
#     # if re.match(r'\d{}, \d{}', contact):
#     Name, Phone = contact.split(',')
#     if Phone not in contacts_ls.keys():
#         contacts_ls.setdefault(Phone, Name)
#     else:
#         print('Контакт с таким номером уже есть!')
#     # else:
#     #     print('Неверный формат ввода!')
#
# def show_contact() -> None:
#     Phone = input('Введите данные контакта (Phone)')
#     if Phone in contacts_ls.keys():
#         print(f'Имя: {contacts_ls[Phone]}, Телефон: {Phone}')
#     else:
#         print('Такого контакта нет!')
#
# def del_contact() -> None:
#     Phone = input('Введите данные контакта (Phone)')
#     if Phone in contacts_ls.keys():
#         contacts_ls.pop(Phone)
#         print(f'Контакт {Phone} удален!')
#     else:
#         print('Такого контакта нет!')
#
# def re_contact() -> None:
#     Phone = input('Введите данные контакта (Phone)')
#     if Phone in contacts_ls.keys():
#         contacts_ls.pop(Phone)
#         contact = input('Введите новые данные контакта (Name,Phone)')
#         Name, Phone = contact.split(',')
#         contacts_ls.setdefault(Phone, Name)
#     else:
#         print('Такого контакта нет!')
#
#
#
#
#
# def main() -> None:
#     while True:
#         choice = input('1-Добавить контакт в формате Имя телефон\n'
#                        '2-Показать контакт\n'
#                        '3-Удалить контакт\n'
#                        '4-Редактирование контакта ->')
#         if choice == '1':
#             add_contact()
#         elif choice == '2':
#             show_contact()
#         elif choice == '3':
#             del_contact()
#         elif choice == '4':
#             re_contact()
#         else:
#             print('Такого пункта меню нет!')
#
#
#
# main()

# def info_man(name, age):
#     print(name, age)
#
# data = {'name': 'Ivan', 'age': 22}
#
# info_man(**data)
# def info_man_2(age, name ):
#     print(name, age)
#
#
# list_info = ['ivan', 18]
#
# info_man_2(*list_info)

# names_list = ['Ivan', 'Anna', 'Maria', 'Sasha']
# names_dict = {key: [] for  key in names_list}
# print(names_dict)

# names_list = ['Ivan', 'Anna', 'Maria', 'Sasha']
# names_dict = {i + 1: names_list[i] for  i in range(len(names_list))}
# print(names_dict)

names_list = ["Ivan", "Anna", "Maria", "Sasha"]
names_dict = {i: [j for j in i] for i in names_list}
print(names_dict)
