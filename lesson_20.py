#
# class Node:
#     def __init__(self, value, right=None, left=None):
#         self.value = value
#         self.right = right
#         self.left = left
#
# class BinaryTree:
#
#     def __init__(self, root):
#         self.root = root
#
#     def bfs(self, node):
#         """
#         Breadth-first-search
#         Обход в ширину
#         :return:
#         """
#         if node is None:
#             return
#
#         queue = [node]
#         while queue:
#             new_level = []
#             for i_node in queue:
#                 print(i_node.value)
#                 if i_node.left:
#                     new_level.append(i_node.left)
#                 if i_node.right:
#                     new_level.append(i_node.right)
#             queue = new_level
#
#     def dfs(self, node):
#         """
#         Deapth-first-search
#         Обход в глубину
#         :param node:
#         :return:
#         """
#         if node is None:
#             return
#         self.dfs(node.right)
#         print(node.value)
#         self.dfs(node.left)
#
#     def min_Depth(self):
#         if not self.root:
#             return 0
#         queue = [self.root]
#         cur_level = 0
#         while queue:
#             cur_level += 1
#             for i_node in range(len(queue)):
#                 cur_node = queue.pop(0)
#                 if cur_node.left or cur_node.right:
#                     if cur_node.left:
#                         queue.append(cur_node.left)
#                     if cur_node.right:
#                         queue.append(cur_node.right)
#                 else:
#                     return cur_level
#         return cur_level
#
#
#
# root = Node(10)
# node_1 = Node(5)
# root.left = node_1
# node_2 = Node(7)
# node_1.right = node_2
# node_3 = Node(16)
# root.right = node_3
# node_4 = Node(13)
# node_3.left = node_4
# node_5 = Node(2)
# node_1.left = node_5
# node_6 = Node(20)
# node_3.right = node_6
#
# # print(root.value, root.right.value, root.left.value)
# # print(node_1.value, node_1.right.value, node_1.left.value)
#
# # b_tree = BinaryTree(root)
# # b_tree.bfs(root)
# b_tree = BinaryTree(root)
# # b_tree.dfs(root)
# print(b_tree.min_Depth())

# import hashlib
#
# correct_password = 'dd679c0b9fd408a04148aa7d30c9df393f67b7227f65693fffe0ed6d0f0ade59'
#
# def hash_password(password):
#     hash_function = hashlib.sha256()
#     hash_function.update(password.encode())
#     hashed_string = hash_function.hexdigest()
#     return hashed_string
#
# password = input('введите пароль: ')
# if hash_password(password) == correct_password:
#     print('Пароль верный!')
# else:
#     print('Пароль не верный!')
# print(hash_password('Jwe987'))

# import requests
# import json
# response = requests.get('https://swapi.dev/api/people/1/')
#
# data = json.load(response.text)
# print(data)

import hashlib
import json


def hash_password(password):
    hash_function = hashlib.sha256()
    hash_function.update(password.encode())
    hashed_string = hash_function.hexdigest()
    return hashed_string


def users_check():
    choise = int(input("Выберите пункт:\n1-авторизироваться\n2-зарегистрироваться -> "))
    if choise == 1:
        mail = input("Введите email: ")
        get_user_by_email(mail)
    elif choise == 2:
        mail = input("Введите email: ")
        passsword = input("Введите пароль: ")
        user = set_user_data(mail, passsword)
        return add_new_user_to_file(user)


def set_user_data(email, password):
    user_data = {"email": email, "password": hash_password(password)}
    return user_data


def add_new_user_to_file(user):
    with open("users.json", "r") as file:
        users_list = json.loads(file.read())
        users_list.append(user)
    with open("users.json", "w") as file:
        file.write(json.dumps(users_list, indent=4))


def get_user_by_email(email):
    with open("users.json", "r") as file:
        users_list = json.loads(file.read())
        # print(users_list)
        for i_user in users_list:
            if i_user["email"] == email:
                password = input("Введите пароль: ")
                if hash_password(password) == i_user["password"]:
                    print("Вы авторизировались!")
                    return
                else:
                    print("Пароль не верный!")
                    return
        print("Вас нет в пользователях!")
        return


users_check()
# get_user_by_email('test@mail.ru')

# user = set_user_data('test@mail.ru', '12345')
# add_new_user_to_file(user)
# user_2 = set_user_data('trewq@mail.ru', '54321')
# add_new_user_to_file(user_2)
