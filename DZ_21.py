# # 1 Задание
# class Books:
#
#     def __init__(self, title: str, year: int, publisher: str, genre: str, author: str, price: float):
#         self.title = title
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#
#     def choice(self):
#
#         choice_1 = int(input('1 - Вывести информацию о книге\n2 - Изменить ниформацию о книге -> '))
#         if choice_1 == 1:
#             print(f'Название: {self.title}\nгод выпуска: {self.year}\nиздатель: {self.publisher}\nжанр: {self.genre}\nавтор: {self.author}\nцена: {self.price}')
#         elif choice_1 == 2:
#             choice_set = int(input('Какую информацию необходимо изменить?\n1-название, 2-год выпуска, 3-издатель. 4-жанр, 5-автор, 6-цена -> '))
#             if choice_set == 1:
#                 title_set = input('Введите новое значение: ')
#                 self.title = title_set
#             elif choice_set == 2:
#                 year_set = int(input('Введите новое значение: '))
#                 self.year = year_set
#             elif choice_set == 3:
#                 publisher_set = input('Введите новое значение: ')
#                 self.publisher = publisher_set
#             elif choice_set == 4:
#                 genre_set = input('Введите новое значение: ')
#                 self.genre = genre_set
#             elif choice_set == 5:
#                 author_set = input('Введите новое значение: ')
#                 self.author = author_set
#             elif choice_set == 6:
#                 price_set = float(input('Введите новое значение: '))
#                 self.price = price_set
#             else:
#                 print('Такого пункта нет!')
#                 return self.choice()
#         else:
#             print('Не правильный выбор!')
#         return self.choice()
#
#
#
# Book_1 = Books(title='The Rivals', year=1995, publisher='A & C Black', genre='classic', author='Elizabeth Duthie', price=6.69)
# Book_2 = Books(title='Harry Potter', year=1998, publisher='A. Levine Books', genre='fantosy', author='J. K. Rowling', price=5.48)
# Book_3 = Books(title='Assata', year=1987, publisher='L. Hill', genre='autobiography', author='Assata Shakur', price=3.99)
# Book_4 = Books(title='Black Silk', year=2008, publisher='Aphrodisia', genre='romantic', author='Sharon Page', price=6.02)

# print(Book_1.title)
# Book_1.title = 'opppopo'
# print(Book_1.title)
# Book_1.choice()
# import random
#
#
# # 2 Задание
#
# class Stadium:
#     def __init__(self, name: str, op_date: str, country: str, capacity: int):
#         self.name = name
#         self.op_date = op_date
#         self.country = country
#         self.capacity = capacity
#
#     def choice(self):
#
#         choice_1 = int(input('1 - Вывести информацию о стадионе\n2 - Изменить ниформацию о стадионе -> '))
#         if choice_1 == 1:
#             print(f'Название: {self.name}\nДата открытия: {self.op_date}\nСтрана: {self.country}\nВместимость: {self.capacity}')
#         elif choice_1 == 2:
#             choice_set = int(input('Какую информацию необходимо изменить?\n1-название, 2-открытая дата, 3-страна. 4-вместимость -> '))
#             if choice_set == 1:
#                 name_set = input('Введите новое значение: ')
#                 self.name = name_set
#             elif choice_set == 2:
#                 op_date_set = int(input('Введите новое значение: '))
#                 self.op_date = op_date_set
#             elif choice_set == 3:
#                 country_set = input('Введите новое значение: ')
#                 self.country = country_set
#             elif choice_set == 4:
#                 capacity_set = input('Введите новое значение: ')
#                 self.capacity = capacity_set
#             else:
#                 print('Такого пункта нет!')
#                 return self.choice()
#         else:
#             print('Не правильный выбор!')
#         return self.choice()
#
# Stadium_1 = Stadium(name='Wembley Stadium', op_date=2007, country='London', capacity=90000)
# Stadium_2 = Stadium(name='Old Trafford', op_date=1910, country='Old Trafford', capacity=74031)
# Stadium_3 = Stadium(name='Anfield', op_date=1884, country='Liverpool', capacity=51000)
# Stadium_4 = Stadium(name='Stamford Bridge', op_date=1877, country='London', capacity=40343)
#
# Stadium_1.choice()


# Задание 3
import random
import time


class Warriors:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def action(self):
        self.health -= 20
        return war()


Warrior_1 = Warriors(name="Smith", health=100)
Warrior_2 = Warriors(name="Thomas", health=100)


def war():
    while True:
        print(
            f"{Warrior_1.name}: {Warrior_1.health}\n{Warrior_2.name}: {Warrior_2.health}"
        )
        time.sleep(0.5)
        if Warrior_1.health == 0:
            print(f"Воин {Warrior_2.name} победил воина {Warrior_1.name}!")
            return
        elif Warrior_2.health == 0:
            print((f"Воин {Warrior_1.name} победил воина {Warrior_2.name}!"))
            return
        else:
            if random.randint(1, 2) == 1:
                print(f"Воин {Warrior_1.name} атакует воина {Warrior_2.name}")
                return Warrior_2.action()
            else:
                print(f"Воин {Warrior_2.name} атакует воина {Warrior_1.name}")
                return Warrior_1.action()


war()
