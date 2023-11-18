# class Queue:
#     # FIFo First in First out
#     def __init__(self):
#         self.queue = []
#
#     def add_item(self, item):
#         self.queue.append(item)
#
#     def pop_item(self):
#         if self.queue:
#             self.queue.pop(0)
#
#     def show_queue(self):
#         print(f'Очередь: ', self.queue)
#         return self.queue
#
#
# queue = Queue()
# queue.show_queue()
# queue.add_item(5)
# queue.add_item(4)
# queue.show_queue()
# queue.pop_item()
# queue.show_queue()

# class Stack:
#     # LIFO Last in First out
#     def __init__(self):
#         self.stack = []
#
#     def add_item(self, item):
#         self.stack.append(item)
#
#     def pop_item(self):
#         if self.stack:
#             self.stack.pop(-1)
#
#     def show_stack(self):
#         print(f'Очередь: ', self.stack)
#         return self.stack
#
# stack = Stack()
# stack.show_stack()
# stack.add_item(5)
# stack.add_item(4)
# stack.show_stack()
# stack.pop_item()
# stack.show_stack()


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head):
        self.head = head

    def get_of_nodes(self):
        current = self.head
        while current:
            # print(current.value)
            yield current.value
            # print(current.value)
            current = current.next

    def remove_node(self, value):
        current = self.head
        prev = current
        while current:
            if current.value == value:
                prev.next = current.next
                return
                prev = current
                current = current.next

    def col_uzl(self):
        current = self.head
        t = 0
        while current:
            t += 1
            current = current.next
        return t

    def centr_uzl(self):
        count = self.col_uzl()
        meen = count // 2
        current = self.head
        while meen != 0:
            meen -= 1
            current = current.next
        return current.value

    def new_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def revers(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


head = Node(5)  # Головной узел
node_1 = Node(7)
head.next = node_1
node_2 = Node(8)
node_1.next = node_2
node_3 = Node(15)
node_2.next = node_3
# print(head.value, head.next.value, head.next.next.value, head.next.next.next)

linked_list = LinkedList(head)
# linked_list.get_of_nodes()
# for i in linked_list.get_of_nodes():
#     print(i)
#
#
#     linked_list.col_uzl()
# print(linked_list.col_uzl())
# print(linked_list.centr_uzl())
linked_list.new_head(6)
linked_list.get_of_nodes()
linked_list.revers()
linked_list.get_of_nodes()
