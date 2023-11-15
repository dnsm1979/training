# 1 задание
# num_1 = int(input('Введите число начала диапозона: '))
# num_2 = int(input('Введите число конец диапозона: '))
# for i in range(num_1, num_2):
#  if i % 7  == 0:
#    print(i)

# 2 задание
# num_1 = int(input('Введите число начала диапозона: '))
# num_2 = int(input('Введите число конец диапозона: '))
# t = 0
# for i in range(num_1, num_2 + 1):
#     print(i)
# for j in range(num_2, num_1, -1):
#     print(j)
# for e in range(num_1, num_2 + 1):
#     if e % 7 == 0:
#         print('кратное 7: ', e)
#     elif e % 5 == 0:
#         t += 1
# print('Чисел кратным 5: ', t)

# 3 Задание
num_1 = int(input('Введите число начала диапозона: '))
num_2 = int(input('Введите число конец диапозона: '))
for i in range(num_1, num_2 + 1):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print('Fizz Buzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
