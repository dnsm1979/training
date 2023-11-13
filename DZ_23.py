# # 1 Задание
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#
#     def __eq__(self, other):
#         if isinstance(other, Circle):
#             return self.radius == other.radius
#         else:
#             return 'Сравнение не возможно!'
#
#     def __gt__(self, other):
#         if isinstance(other, Circle):
#             return self.circumference() > other.circumference()
#         else:
#             return 'Сравнение не возможно!'
#
#     def __ge__(self, other):
#         if isinstance(other, Circle):
#             return self.circumference() >= other.circumference()
#         else:
#             return 'Сравнение не возможно!'
#
#     def __lt__(self, other):
#         if isinstance(other, Circle):
#             return self.circumference() < other.circumference()
#         else:
#             return 'Сравнение не возможно!'
#
#     def __le__(self, other):
#         if isinstance(other, Circle):
#             return self.circumference() <= other.circumference()
#         else:
#             return 'Сравнение не возможно!'
#
#     def __add__(self, num):
#         self.radius = self.radius + num
#         return self.circumference()
#
#     def __iadd__(self, num):
#         self.radius += num
#         return self.circumference()
#
#     def __sub__(self, num):
#         self.radius = self.radius - num
#         return self.circumference()
#
#     def __isub__(self, num):
#         self.radius -= num
#         return self.circumference()
#
#
#     def circumference(self):
#         return 2 * math.pi * self.radius
#
#
#
#
# circle_1 = Circle(15)
# circle_2 = Circle(12)
# comparison = circle_1 == circle_2
# print(f'{circle_1.radius} == {circle_2.radius}', comparison)
# comparison = circle_1 > circle_2
# print(f'{circle_1.circumference()} > {circle_2.circumference()}', comparison)
# comparison = circle_1 >= circle_2
# print(f'{circle_1.circumference()} >= {circle_2.circumference()}', comparison)
# comparison = circle_1 < circle_2
# print(f'{circle_1.circumference()} < {circle_2.circumference()}', comparison)
# comparison = circle_1 <= circle_2
# print(f'{circle_1.circumference()} <= {circle_2.circumference()}', comparison)
# result = circle_2 + 5
# print(f'Пропорциональное изменение размеров окружности, путем изменения ее радиуса + ', result)
# result = circle_2 - 10
# print(f'Пропорциональное изменение размеров окружности, путем изменения ее радиуса - ', result)
# circle_1 += 5
# print(f'Пропорциональное изменение размеров окружности, путем изменения ее радиуса += ', circle_1)
# circle_1 -= 10
# print(f'Пропорциональное изменение размеров окружности, путем изменения ее радиуса -= ', circle_1)

# Задание 2

# class Complex:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def complex_num(self):
#         return complex(self.a, self.b)
#
#     def __add__(self, other):
#         return self.complex_num() + other.complex_num()
#
#     def __sub__(self, other):
#         return self.complex_num() - other.complex_num()
#
#     def __mul__(self, other):
#         return self.complex_num() * other.complex_num()
#
#     def __truediv__(self, other):
#         return self.complex_num() / other.complex_num()
#
#
#
# complex_1 = Complex(1, 2)
# complex_2 = Complex(2, 4)
# comparison = complex_1 + complex_2
# print(f'{complex_1.complex_num()} + {complex_2.complex_num()} =', comparison)
# comparison = complex_1 - complex_2
# print(f'{complex_1.complex_num()} - {complex_2.complex_num()} =', comparison)
# comparison = complex_1 * complex_2
# print(f'{complex_1.complex_num()} * {complex_2.complex_num()} =', comparison)
# comparison = complex_1 / complex_2
# print(f'{complex_1.complex_num()} / {complex_2.complex_num()} =', comparison)

# Задание 3

# class Airplane:
#     def __init__(self, type_of_flight: str, occupancy: int, capacity: int):
#         self.type_of_flight = type_of_flight
#         self.occupancy = occupancy
#         self.capacity = capacity
#
#     def __eq__(self, other):
#         if isinstance(other, Airplane):
#             return self.type_of_flight == other.type_of_flight
#         else:
#             return 'Сравнение не возможно!'
#
#     def __add__(self, num):
#         self.occupancy = self.occupancy + num
#         return self.occupancy
#
#     def __sub__(self, num):
#         self.occupancy = self.occupancy - num
#         return self.occupancy
#
#     def __iadd__(self, num):
#         self.occupancy += num
#         return self
#
#     def __isub__(self, num):
#         self.occupancy -= num
#         return self
#
#     def __gt__(self, other):
#         if isinstance(other, Airplane):
#             return self.capacity > other.capacity
#         else:
#             return 'Сравнение не возможно!'
#
#     def __lt__(self, other):
#         if isinstance(other, Airplane):
#             return self.capacity < other.capacity
#         else:
#             return 'Сравнение не возможно!'
#
#     def __ge__(self, other):
#         if isinstance(other, Airplane):
#             return self.capacity >= other.capacity
#         else:
#             return 'Сравнение не возможно!'
#
#     def __le__(self, other):
#         if isinstance(other, Airplane):
#             return self.capacity <= other.capacity
#         else:
#             return 'Сравнение не возможно!'
#
#
#
# airplane_1 = Airplane('cargo', 200, 250)
# airplane_2 = Airplane('charter', 150, 300)
# comparison = airplane_1 == airplane_2
# print(f'Проверка на равенство типов самолетов: {airplane_1.type_of_flight} == {airplane_2.type_of_flight} -> ',comparison)
# print(f'Текущее количество пассажиров в самолете: ', airplane_1.occupancy)
# occupancy_add = airplane_1 + 50
# print(f'Текущее количество пассажиров в самолете после добовления: ',occupancy_add)
# print(f'Текущее количество пассажиров в самолете: ', airplane_1.occupancy)
# occupancy_sub = airplane_1 - 50
# print(f'Текущее количество пассажиров в самолете после вычитания: ',occupancy_sub)
# print(f'Текущее количество пассажиров в самолете: ', airplane_2.occupancy)
# airplane_2 += 150
# print(f'Текущее количество пассажиров в самолете после добовления: ', airplane_2.occupancy)
# print(f'Текущее количество пассажиров в самолете: ', airplane_2.occupancy)
# airplane_2 -= 250
# print(f'Текущее количество пассажиров в самолете после вычитания: ', airplane_2.occupancy)
# comparison = airplane_1 > airplane_2
# print(f'Сравнение двух самолетов по максимально возможному количеству пассажиров на борту: {airplane_1.capacity} > {airplane_2.capacity} -> ', comparison)
# comparison = airplane_1 < airplane_2
# print(f'Сравнение двух самолетов по максимально возможному количеству пассажиров на борту: {airplane_1.capacity} < {airplane_2.capacity} -> ', comparison)
# comparison = airplane_1 >= airplane_2
# print(f'Сравнение двух самолетов по максимально возможному количеству пассажиров на борту: {airplane_1.capacity} >= {airplane_2.capacity} -> ', comparison)
# comparison = airplane_1 <= airplane_2
# print(f'Сравнение двух самолетов по максимально возможному количеству пассажиров на борту: {airplane_1.capacity} <= {airplane_2.capacity} -> ', comparison)

# Задание 4
class Flat:
    def __init__(self, area, price, floor):
        self.aria = area
        self.price = price
        self.floor = floor

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.aria == other.aria
        else:
            return 'Сравнение не возможно!'
    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.aria != other.aria
        else:
            return 'Сравнение не возможно!'

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price > other.price
        else:
            return 'Сравнение не возможно!'

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price < other.price
        else:
            return 'Сравнение не возможно!'

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price >= other.price
        else:
            return 'Сравнение не возможно!'

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price <= other.price
        else:
            return 'Сравнение не возможно!'


flat_1 = Flat(60, 5000000, 8)
flat_2 = Flat(58, 5000000, 5)

comparison = flat_1 == flat_2
print(f'Проверка на равенство площадей квартир: {flat_1.aria} == {flat_2.aria} -> ', comparison)
comparison = flat_1 != flat_2
print(f'Проверка на равенство площадей квартир: {flat_1.aria} != {flat_2.aria} -> ', comparison)

comparison = flat_1 > flat_2
print(f'Сравнение двух квартир по цене: {flat_1.price} > {flat_2.price} -> ', comparison)
comparison = flat_1 < flat_2
print(f'Сравнение двух квартир по цене: {flat_1.price} > {flat_2.price} -> ', comparison)
comparison = flat_1 >= flat_2
print(f'Сравнение двух квартир по цене: {flat_1.price} >= {flat_2.price} -> ', comparison)
comparison = flat_1 <= flat_2
print(f'Сравнение двух квартир по цене: {flat_1.price} <= {flat_2.price} -> ', comparison)


