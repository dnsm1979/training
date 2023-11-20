# 1. Генераторное выражение выдающее квадраты чисел из заданного
# диапазона чисел.
# def generation(start, end):
#     for i in range(start, end + 1):
#         yield i ** 2
#
# for i in generation(2, 10):
#     print(i)

# 2. Генераторная функция принимающая начало и конец диапазона,
# и выдающая только простые числа.

# def gen_isprime(start, end):
#     k = 0
#     for i in range(start, end + 1):
#
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             yield i
#
#
# for i in gen_isprime(1, 20):
#     print(i)
# 3*. Класс-итератор выдающий только чётные числа из заданного диапазона


class genetation:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.cur = start - 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        # print('__next__')

        if self.cur == self.end:
            raise StopIteration
        self.cur += 1
        if self.cur % 2 == 0:
            return self.cur


for i in genetation(10, 20):
    print(i)
