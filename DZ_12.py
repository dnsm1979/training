list_1 = [1, 3, 6, 78, 89, 90, 33]
list_2 = [1, 2, 3, 4, 5, 10, 99, 33]
# 1. список, содержащий элементы
# обоих списков
# list_3 = list_1 + list_2
# print(list_3)
# 2. список, содержащий элементы
# обоих списков без повторений
# list_3 = list_1
# for i in range(len(list_2)):
#     if list_2[i] not in list_1:
#         list_3.append(list_2[i])
# print(list_3)
# 3. список, содержащий элементы
# общие для двух списков
# list_3 = []
# for i in range(len(list_2)):
#     if list_2[i] in list_1:
#         list_3.append(list_2[i])
# print(list_3)
# 4. список, содержащий только уникальные элементы каждого из списков
list_3 = []
for i in range(len(list_2)):
    if list_2[i] not in list_1:
        list_3.append(list_2[i])
for i in range(len(list_1)):
    if list_1[i] not in list_2:
        list_3.append(list_1[i])
print(list_3)
# 5. список, содержащий только
# минимальное и максимальное значение каждого из
# списков
# list_3 = []
# list_3.append(min(list_1))
# list_3.append(min(list_2))
# list_3.append(max(list_1))
# list_3.append(max(list_2))
# print(list_3)
