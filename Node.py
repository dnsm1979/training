import random
import math


# класс Node для определения элемента списка
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = "LinkedList [\n" + str(current.value) + "\n"
            while current.next != None:
                current = current.next
                out += str(current.value) + "\n"
            return out + "]"
        return "LinkedList []"

    def clear(self):
        self.__init__()

    # добавление в конец списка
    def add(self, x):
        self.length += 1
        if self.first == None:
            # self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
        else:
            # здесь, уже на разные, т.к. произошло присваивание
            self.last.next = self.last = Node(x, None)

    # добавление в произвольное место
    def InsertNth(self, i, x):
        if self.first == None:
            self.last = self.first = Node(x, None)
            return
        if i == 0:
            self.first = Node(x, self.first)
            return
        curr = self.first
        count = 0
        while curr != None:
            count += 1
            if count == i:
                curr.next = Node(x, curr.next)
                if curr.next.next == None:
                    self.last = curr.next
                break
            curr = curr.next

    # удаление элемента
    def Del(self, i):
        if self.first == None:
            return
        curr = self.first
        count = 0
        if i == 0:
            self.first = self.first.next
            return
        while curr != None:
            if count == i:
                if curr.next == None:
                    self.last = curr
                old.next = curr.next
                break
            old = curr
            curr = curr.next
            count += 1


# проверяем работу алгоритма
l = LinkedList()
for i in range(10):
    l.add(random.randint(0, 10))

print(l)

l.InsertNth(3, 100)
print(l)

l.Del(0)
print(l)
