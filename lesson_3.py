# import time
# for i in range(10):
#     time.sleep(1)
#     print(i)
# for i in range(10):
#     print('Привет!')
# for i in 'python':
#     print(i + '*', end='')
# for i in range(0, 5):
#     if i == 3:
#         break
#         print(i)
#     else:
#         print('ok')
# start = int(input('Введите начало: '))
# end = int(input('Введите конец: '))
# for i in range(start, end + 1):
#     if i % 2 == 0:
#         print(f'{i} является четным!')

# start = int(input('Введите начало: '))
# end = int(input('Введите конец: '))
# for i in range(end, start -1, -1):
#     print(i)
# start = int(input('Введите начало: '))
# end = int(input('Введите конец: '))
# summa = 0
# for i in range(1, 200):
#     summa += i
# print(summa)
# number = int(input('Введите число: '))
# factorial = 1
# for i in range(2, number + 1):
#     factorial *= i
# print(f'факториал числа {number} равен {factorial}')

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end='\t')
#     print()

# correct_pin = 1547
# for i in range(3):
#     pin = int(input('Введите пин-код: '))
#     if pin == correct_pin:
#         print('Пин-код верный!')
#         break
#     else:
#         print('Повторите попытку!')
# else:
#     print('ЗАКОНЧИЛИСЬ ПОПЫТКИ ВВОДА!')
# summa = 0
# t = 0
# number_1 = int(input('Введите первое число: '))
# number_2 = int(input('Введите второе число: '))
# for i in range( number_1, number_2 + 1):
#     summa += i
#     t += 1
#
# print(summa, summa / t )
# line = int(input('Введите отрезок: '))
# for i in range(line + 1):
#     print('*', end='')

# line = int(input('Введите отрезок: '))
# simbol = str(input('Введите символ отображения: '))
# for i in range(line + 1):
#     print(simbol, end='')
# numter = int(input('Введите число от 1 до 9: '))
# for i in range(1, 10):
#     print(numter, '*', i, '=', numter * i)

start = int(input('Введите первое число диапозона: '))
end = int(input('Введите второе число диапозона: '))
number = int(input('Введите число: '))
for i in range(start, end + 1):
    if i == number:
        print(f'!{i}!', end=' ')
        continue
    print(i, end=' ')
