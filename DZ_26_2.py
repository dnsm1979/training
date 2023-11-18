# 1 задание работа со списком пользователя
def start_menu():
    func_start_menu = [
        add_number_to_user_list,
        del_all_number_in_user_list,
        show_sub_menu,
        check_number_in_user_list,
        replace_sub_menu,
    ]
    choice = int(
        input(
            f"1-Добавить новое число в список\n"
            f"2-Удалить число(числа) из списка\n"
            f"3-Показать содержимое списка\n"
            f"4-Проверить есть ли число в списке\n"
            f"5-Заменить значение в списке\n"
            f"0-Выход -> "
        )
    )
    if choice == 0:
        return
    elif 1 <= choice <= 5:
        return func_start_menu[choice - 1]()
    else:
        print("Такого пункта нет!")


def show_sub_menu():
    choice = int(
        input(
            f"1-Показать содержимое списка с начала\n"
            f"2-Показать содержимое списка с конца\n"
        )
    )
    if choice == 1:
        print(user_list)
    elif choice == 2:
        print(user_list[::-1])
    else:
        print("Такого пункта нет!")
    return start_menu()


def replace_sub_menu():
    choice = int(
        input(f"1-Заменить только первое вхождение\n" f"2-Заменить все вхождения\n")
    )
    if choice == 1:
        return replase_number_in_user_list(
            int(input("Число: ")), int(input("Новое число: "))
        )
    elif choice == 2:
        return replase_all_number_in_user_list(
            int(input("Число: ")), int(input("Новое число: "))
        )
    else:
        print("Такого пункта нет!")
        return start_menu()


user_list = []


def add_user_list(*arcs):
    global user_list
    for i in arcs:
        user_list.append(i)

    return start_menu()


def add_number_to_user_list():
    number = int(input("Введите число: "))
    if number in user_list:
        print("Такое число уже есть в списке!")
        return start_menu()
    else:
        user_list.append(number)
        print(f"Число {number} добавлено в список!")
        return start_menu()


def del_number_in_user_list():
    number = int(input("Введите число: "))
    if number in user_list:
        user_list.remove(number)
        print(f"Первое вхождение {number} удалено из списка!")
        return start_menu()
    print(f"Числа {number} нет в списке!")
    return start_menu()


def del_all_number_in_user_list():
    number = int(input("Введите число: "))
    if number in user_list:
        while number in user_list:
            user_list.remove(number)
        print(f"Все числа {number} удалены из списка!")
        return start_menu()
    else:
        print(f"Числа {number} нет в списке!")
        return start_menu()


def check_number_in_user_list():
    number = int(input("Введите число: "))
    count = 0
    if number in user_list:
        for i in user_list:
            if i == number:
                count += 1
        print(f"{number} встречается в списке {count} раз(а)!")
        return start_menu()
    else:
        print(f"Числа {number} нет в списке!")
        return start_menu()


def replase_number_in_user_list(number, new_number):
    if number in user_list:
        for i in range(len(user_list)):
            if user_list[i] == number:
                user_list[i] = new_number
                print(f"Первое попавшееся число {number} заменено на {new_number}!")
                return start_menu()
    else:
        print(f"Числа {number} нет в списке!")
        return start_menu()


def replase_all_number_in_user_list(number, new_number):
    if number in user_list:
        for i in range(len(user_list)):
            if user_list[i] == number:
                user_list[i] = new_number
        print(f"Числа {number} заменены на {new_number}!")
        return start_menu()
    else:
        print(f"Числа {number} нет в списке!")
        return start_menu()


add_user_list(5, 6, 8, 9, 77, 55, 5, 9, 5)

# 2 задание: класс стека для работы со строками (стек строк)
# class Stack:
#
#
#     def __init__(self):
#         self.stack = []
#         self.size = 100
#
#     def add_item(self):
#         if self.stack == self.size:
#             return f'Стек полон!'
#         else:
#             item = (input('-> '))
#             self.stack.append(item)
#
#     def pop_item(self):
#         if self.stack:
#             self.stack.pop()
#
#     def show_stack(self):
#         return f'Очередь: ', self.stack
#
#     def score_ctack(self):
#         print(f'Количество строк в стеке: {len(self.stack)}')
#         return self.stack
#
#     def isEmpty(self):
#         if len(self.stack) == 0:
#             print('Стек пустой!')
#             return self.stack
#         print('Стек не пустой')
#         return self.stack
#
#     def isFull(self):
#         if self.stack == self.size:
#             print(f'Стек полный!')
#             return self.stack
#         else:
#             print(f'Стек не полный!')
#             return self.stack
#
#     def clear_stack(self):
#         while len(self.stack) > 0:
#             self.stack.pop()
#         print(f'Стек очищен! ')
#         return self.stack
#
#     def peek(self):
#         if len(self.stack) == 0:
#             print('Стек пустой')
#             return self.stack
#         print(self.stack[len(self.stack)-1])
#         return self.stack
#
#     def menu(self):
#
#
#         choice = int(input('1-помещение строки в стек\n'
#                            '2-выталкивание строки из стека\n'
#                            '3-подсчет количества строк в стеке\n'
#                            '4-проверку пустой ли стек\n'
#                            '5-проверку полный ли стек\n'
#                            '6-очистку стека\n'
#                            '7-получение значения без выталкивания верхней строки из стека -> '))
#         if choice == 1:
#             return self.add_item()
#         elif choice == 2:
#             self.pop_item()
#         elif choice == 3:
#             return self.score_ctack()
#         elif choice == 4:
#             return self.isEmpty()
#         elif choice == 5:
#             return self.isFull()
#         elif choice == 6:
#             return self.clear_stack()
#         elif choice == 7:
#             return self.peek()
#         else:
#             return f'Такого пункта нет!'
#
# stack = Stack()
# while True:
#     stack.menu()


#  3 задание: стек из второго задания, таким образом,
# чтобы его размер был нефиксированным.
# from collections import deque
#
# class Deque:
#
#
#     def __init__(self):
#         self.stack = deque()
#
#
#     def add_item(self):
#         item = input('-> ')
#         self.stack.append(item)
#         print('Строка добавлена в стек!')
#
#     def pop_item(self):
#         if self.stack:
#             self.stack.pop()
#             print('последняя строка вытолкнута!')
#
#     def show_stack(self):
#         return f'Очередь: ', self.stack
#
#     def score_ctack(self):
#         print(f'Количество строк в стеке: {len(self.stack)}')
#         return self.stack
#
#     def isEmpty(self):
#         if len(self.stack) == 0:
#             print('Стек пустой!')
#             return self.stack
#         print('Стек не пустой')
#         return self.stack
#
#
#     def clear_stack(self):
#         while len(self.stack) > 0:
#             self.stack.pop()
#         print(f'Стек очищен! ')
#         return self.stack
#
#     def peek(self):
#         if len(self.stack) == 0:
#             print('Стек пустой')
#             return self.stack
#         print(self.stack[len(self.stack)-1])
#         return self.stack
#
#     def menu(self):
#
#         choice = int(input('1-помещение строки в стек\n'
#                            '2-выталкивание строки из стека\n'
#                            '3-подсчет количества строк в стеке\n'
#                            '4-проверку пустой ли стек\n'
#                            '5-очистку стека\n'
#                            '6-получение значения без выталкивания верхней строки из стека -> '))
#         if choice == 1:
#             return self.add_item()
#         elif choice == 2:
#             return self.pop_item()
#         elif choice == 3:
#             return self.score_ctack()
#         elif choice == 4:
#             return self.isEmpty()
#         elif choice == 5:
#             return self.clear_stack()
#         elif choice == 6:
#             return self.peek()
#         else:
#             return f'Такого пункта нет!'
#
# stack = Deque()
# while True:
#     stack.menu()
