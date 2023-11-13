# # 1 задание
# def nums_ls(*args):
#     t = 1
#     for i in range(len(args)):
#     		t *= args[i]
#     print(f'Произведение чисел списка: {t}')
# nums_ls(2, 3, 4, 5)
# # 2 задание
# def nums_ls(*args):
#     t = []
#     for i in range(len(args)):
#     	t.append(args[i])
#     print(f'Минимальное значение в спмске: {min(t)}')
# nums_ls( 8, 3, 4, 5)
# # 3 задание
# def nums_ls(*args):
#     t = 0
#     for x in range(len(args)):
#         simple = True
#         for j in range(2, args[x]):
#             if args[x] % j == 0:
#                 simple = False
#                 break
#         if simple:
#             t += 1
#             print(args[x])
#     print(f'Простых чисел в списке: {t}')
#
# nums_ls(8, 3, 4, 9, 5)
# 4 задание
# def nums(num_del, *args):
#     print(args)
#     num_ls = []
#     t = 0
#     for i in range(len(args)):
#         if num_del == args[i]:
#             t += 1
#         else:
#             num_ls.append(args[i])
#     print(f'Удаленных чисел в списке: {t}')
#     print (tuple(num_ls))
#
# nums(3, 4, 8, 9, 2, 6 ,3, 7, 3, 3)
# # 5 Задание
# def Lists(ls_1, ls_2):
#     print(f'Первый список: {ls_1}'), print(f'Второй список: {ls_2}')
#     list_3  = ls_1 + ls_2
#     print(f'Объединенный список: {list_3}')
#
#
#
# Lists((5, 6, 3, 'rt', 'fg'), (7, 8, 8, 9))
# 6 Задание
def exp_num_ls(exp, *nums):
    num_ls = []
    for i in range(len(nums)):
        num_ls.append(nums[i] ** exp)

    print(f'Новый список элементов в степени {exp}: {num_ls}')

exp_num_ls(2, 2, 3, 4, 5, 6)

