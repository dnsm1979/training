# 1 Задание


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"[{self.data}]->{self.next}"


class Num_list:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        if self.head != None:
            out = "Num_list [\n" + str(current.value) + "\n"
            while current.next != None:
                current = current.next
                out += str(current.value) + "\n"
            return out + "]"
        return "Num_list []"

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def insert_by_index(self, value, index):
        if index == 0:
            self.add_first(value)
            return
        new_node = Node(value)
        node_number = 1
        current_node = self.head
        while current_node is not None:
            if index == node_number:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
            node_number += 1

    def delet_by_index(self, index):
        if index == 0:
            self.delete_first()
            return
        node_number = 0
        current_node = self.head
        previous_node = current_node
        while current_node is not None:
            if index == node_number:
                previous_node.next = current_node.next
                current_node.next = None
                return
            previous_node = current_node
            current_node = current_node.next
            node_number += 1

    def set_value_by_index(self, value, index):
        node_number = 0
        current_node = self.head
        while current_node is not None:
            if node_number == index:
                current_node.data = value
                return self.menu()
            current_node = current_node.next
            node_number += 1

    def delete_last(self):
        if self.head is Num_list or self.head.next is None:
            self.head = None
            return
        current_node = self.head
        previous_node = current_node
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None

    def delete_first(self):
        if self.head is None:
            return self.menu()
        self.head = self.head.next

    def get_length(self):
        length = 0
        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length

    def print_list(self):
        result = ""
        current_node = self.head
        while current_node is not None:
            result += str(current_node.data) + " -> "
            current_node = current_node.next
        else:
            result += "None"
            print(result)

    def input_list(self):
        list_l = Num_list()
        list_node = input("Введите занчения через пробел: ").split()
        for i_node in list_node:
            list_l.add_last(i_node)

    def menu(self):
        choice = int(
            input(
                f"Выберите один из пунктов:\n1-Добавить элемент в список.\n2-Удалить элемент из списка.\n"
                f"3-Показать содержимое списка.\n4-Проверить есть ли значение в списке.\n"
                f"5-Заменить значение в списке. -> "
            )
        )
        if choice == 1:
            return self.menu_add()
        elif choice == 2:
            return self.menu_delete()
        elif choice == 3:
            return self.print_list()
        elif choice == 4:
            return self.set_value_by_index()
        elif choice == 5:
            return self.removed_node()
        else:
            print("Такого пункта нет!")
            return

    def menu_add(self):
        choice = int(
            input("1-Добавить в начало\n2-Добавить в конец\n3-Добавить по индексу --> ")
        )
        if choice == 1:
            return self.add_first(input("Введите значение нового элемента: "))
        elif choice == 2:
            return self.add_last(input("Введите значение нового элемента: "))
        elif choice == 3:
            return self.insert_by_index(
                input("Введите индекс элемента: "), input("Введите индекс элемента: ")
            )
        else:
            print("Такого пункта нет!")
            return

    def menu_delete(self):
        choice = int(
            input("1-Удалить из начала\n2-Удалить в конце\n3-Удалить по индексу --> ")
        )
        if choice == 1:
            return self.delete_first()
        elif choice == 2:
            return self.delete_last()
        elif choice == 3:
            return self.delet_by_index(input("Введите индекс элемента: "))
        else:
            print("Такого пункта нет!")
            return

    def removed_node(self):
        value = input("Введите значение элемента: ")
        index = input("Введите индекс элемента: ")
        self.delet_by_index(index)
        self.insert_by_index(value, index)
        return


ls_1 = Num_list().input_list()
ls = Num_list
print(ls_1)
