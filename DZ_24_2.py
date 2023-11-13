class Node:
    element = None
    next_node = None

    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node


class LinkedList:
    head = None
    length = 0

    def append(self, element):
        if not self.head:
            self.head = Node(element)
            self.length += 1
            return element
        node = self.head
        while node.next_node:
            node = node.next_node

        node.next_node = Node(element)
        self.length += 1
        return element

    def __str__(self):
        node = self.head
        line = '['
        while node.next_node:
            line += str(node.element)+', '
            node = node.next_node
        line += str(node.element)+']'
        return line

    def pr_menu(self):
        current = self.head
        while current:

              print(current.element)
              current = current.next_node
        return current.element


    def __getitem__(self, key):
        i = 0
        node = self.head
        while i < key:
            node = node.next_node
            i += 1
        return node.element

    def insert(self, key, value):
        i = 0
        node = self.head
        prev_node = self.head
        if key == 0:
            old_head = self.head
            self.head = Node(value, next_node=old_head)
            return value
        while i < key:
            prev_node = node
            node  = node.next_node
            i += 1

        prev_node.next_node = Node(value, next_node=node)
        self.length += 1
        return value
    def __delitem__(self, key):
        i = 0
        node = self.head
        prev_node = node
        if key == 0:
            old_head = self.head
            element = self.head.element
            self.head = self.head.next_node
            self.length -= 1
            del old_head
            return element
        while i < key:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = node.next_node
        element = node.element
        self.length -= 1
        del node
        return element

    def search_elements(self, element):
        current = self.head
        i = 0
        while current is not None:
            if current.element == element:
                print(f'Элемент {element} присутствует в списке по индексу {i}!')
                return
            current = current.next_node
            i += 1

        print('Элемента нет в списке!')

    def remove_element(self, element, element_new):
        current = self.head
        i = 0
        while current is not None:
            if current.element == element:

                self.__delitem__(key=i)
                # self.insert(key=i, value=element_new)
                print(f'Элемент {element} заменен на {element_new}!')
                return self.insert(key=i, value=element_new)
            current = current.next_node
            i += 1

        print('Элемента нет в списке!')



    def menu(self):

        choice = int(input(f'Выберите один из пунктов:\n1-Добавить элемент в список.\n2-Удалить элемент из списка.\n'
                           f'3-Показать содержимое списка.\n4-Проверить есть ли значение в списке.\n'
                           f'5-Заменить значение в списке. -> '))
        if choice == 1:
           self.append(input('Введите новый элемент: '))
        elif choice == 2:
            del_el = int(input('Введите индекс удаляемого элемента: '))
            del a[del_el]
            # self.__delitem__(key=int(del_el))
        elif choice == 3:
            return print(a)
        elif choice == 4:
            self.search_elements(input('Введите искомый элемент: '))
        elif choice == 5:
            el = input('Заменяемый элемент: ')
            el_new = input('Новый элемент: ')
            self.remove_element(el, el_new)
        else:
            print('Такого пункта нет!')


a = LinkedList()
list_node = input('Введите занчения через пробел: ').split()
for i_node in list_node:
    a.append(i_node)

print(a)

while True:
    a.menu()


# 2 Задание
#
# class Node:
#     element = None
#     next_node = None
#     prev_node = None
#
#     def __init__(self, element, next_node=None, prev_node=None):
#         self.element = element
#         self.next_node = next_node
#         self.prev_node = prev_node
#
#
# class LinkedList:
#     head = None
#     length = 0
#
#     def append(self, element):
#         if not self.head:
#             self.head = Node(element)
#             self.length += 1
#             return element
#         node = self.head
#         prev = self.head
#
#         while node.next_node:
#             prev.prev_node = node
#             node = node.next_node
#
#         node.next_node = Node(element)
#         self.length += 1
#         return element
#
#     def __str__(self):
#         node = self.head
#         line = '['
#         while node.next_node:
#             line += str(node.element)+' '
#             node = node.next_node
#         line += str(node.element)+']'
#         return line
#
#
#     def __getitem__(self, key):
#         i = 0
#         node = self.head
#         while i < key:
#             node = node.next_node
#             i += 1
#         return node.element
#
#     def insert(self, key, value):
#         i = 0
#         node = self.head
#         prev_node = self.head
#         prev_current = self.head
#         if key == 0:
#             old_head = self.head
#             self.head = Node(value, next_node=old_head)
#             return value
#         while i < key:
#             prev_current = prev_node
#             prev_node = node
#             node = node.next_node
#             i += 1
#
#         prev_node.next_node = Node(value, next_node=node, prev_node=prev_current)
#         # node.prev_node = prev_node
#         self.length += 1
#         return value
#
#     def __delitem__(self, key):
#         i = 0
#         node = self.head
#         prev_node = node
#         if key == 0:
#             old_head = self.head
#             element = self.head.element
#             self.head = self.head.next_node
#             self.length -= 1
#             del old_head
#             return element
#         while i < key:
#             prev_node = node
#             node = node.next_node
#             i += 1
#
#         prev_node.next_node = node.next_node
#         node.prev_node = prev_node
#         element = node.element
#         self.length -= 1
#         del node
#         return element
#
#     def search_elements(self, element):
#         current = self.head
#         i = 0
#         while current is not None:
#             if current.element == element:
#                 print(f'Элемент {element} присутствует в списке по индексу {i}!')
#                 return
#             current = current.next_node
#             i += 1
#
#         print('Элемента нет в списке!')
#
#     def remove_element(self, element, element_new):
#         current = self.head
#         i = 0
#         while current is not None:
#             if current.element == element:
#
#                 self.__delitem__(key=i)
#                 # self.insert(key=i, value=element_new)
#                 print(f'Элемент {element} заменен на {element_new}!')
#                 return self.insert(key=i, value=element_new)
#             current = current.next_node
#             i += 1
#
#         print('Элемента нет в списке!')
#
#
#
#     def menu(self):
#
#         choice = int(input(f'Выберите один из пунктов:\n1-Добавить строку в список.\n2-Удалить строку из списка.\n'
#                            f'3-Показать содержимое списка.\n4-Проверить есть ли строка в списке.\n'
#                            f'5-Заменить строку в списке. -> '))
#         if choice == 1:
#            self.append(input('Введите новую строку: '))
#         elif choice == 2:
#             del_el = int(input('Введите индекс удаляемой строки: '))
#             del a[del_el]
#             # self.__delitem__(key=int(del_el))
#         elif choice == 3:
#             return print(a)
#         elif choice == 4:
#             self.search_elements(input('Введите искомую строку: '))
#         elif choice == 5:
#             el = input('Заменяемая строка: ')
#             el_new = input('Новая строка: ')
#             self.remove_element(el, el_new)
#         else:
#             print('Такого пункта нет!')
#
#
# a = LinkedList()
# list_node = input('Введите строки разделяя пробелами: ').split()
# for i_node in list_node:
#     a.append(i_node)
#
# print(a)
#
# while True:
#     a.menu()

# 3 Задание

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
#             item = int(input('-> '))
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
#         print(f'Количество чисел в стеке: {len(self.stack)}')
#         return self.stack
#
#     def isEmpty(self):
#         if len(self.stack) == 0:
#             print('Стек пустой!')
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
#         print(self.stack[len(self.stack)-1])
#         return self.stack
#
#     def menu(self):
#

#         choice = int(input('1-помещение целого значения в стек\n'
#                            '2-выталкивание целого значения из стека\n'
#                            '3-подсчет количества целых в стеке\n'
#                            '4-проверку пустой ли стек\n'
#                            '5-проверку полный ли стек\n'
#                            '6-очистку стека\n'
#                            '7-получение значения без выталкивания верхнего целого в стеке. -> '))
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


# # 4 задание
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
#         item = int(input('-> '))
#         self.stack.append(item)
#
#     def pop_item(self):
#         if self.stack:
#             self.stack.pop()
#
#     def show_stack(self):
#         return f'Очередь: ', self.stack
#
#     def score_ctack(self):
#         print(f'Количество чисел в стеке: {len(self.stack)}')
#         return self.stack
#
#     def isEmpty(self):
#         if len(self.stack) == 0:
#             print('Стек пустой!')
#         print('Стек не пустой')
#         return self.stack
#
#     def isFull(self):
#         if self.stack.append(0):
#             print(f'Стек не полный!')
#             self.stack.pop()
#             return self.stack
#         else:
#             print(f'Стек полный!')
#             return self.stack
#
#     def clear_stack(self):
#         while len(self.stack) > 0:
#             self.stack.pop()
#         print(f'Стек очищен! ')
#         return self.stack
#
#     def peek(self):
#         print(self.stack[len(self.stack)-1])
#         return self.stack
#
#     def menu(self):
#
#         choice = int(input('1-помещение целого значения в стек\n'
#                            '2-выталкивание целого значения из стека\n'
#                            '3-подсчет количества целых в стеке\n'
#                            '4-проверку пустой ли стек\n'
#                            '5-проверку полный ли стек\n'
#                            '6-очистку стека\n'
#                            '7-получение значения без выталкивания верхнего целого в стеке. -> '))
#         if choice == 1:
#             return self.add_item()
#         elif choice == 2:
#             return self.pop_item()
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
# stack = Deque()
# while True:
#     stack.menu()