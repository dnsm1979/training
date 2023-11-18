# class Point:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     def __init__(self, x, y):
#         self.set_coordinates(x, y)
#
#     @classmethod
#     def set_square(cls, left, right):
#         cls.MIN_COORD = left
#         cls.MAX_COORD = right
#
#     def set_coordinates(self, x, y):
#         if Point.MIN_COORD <= x <= Point.MAX_COORD and Point.MIN_COORD <= y <= Point.MAX_COORD:
#             self.x = x
#             self.y = y
#         else:
#             print('Точка лежит вне области!')
#
#
#     def __setattr__(self, key, value):
#         print('Сработал __setattr__')
#         if key =='w':
#             raise ValueError('Недопустимое значение атрибута!')
#         object.__setattr__(self, key, value)
#
#     def __getattribute__(self, item):
#         print('Сработал метод __getattribute__')
#         if item == 'x':
#             raise ValueError('У вас нет доступа к значению этого атрибута!')
#         return object.__getattribute__(self, item)
#
#     def __str__(self):
#         return f'Коордтнаты точки: x={self.x}, y={self.y}'
#
# # point_1 = Point(1, 1)
# #
# # point_1.MIN_COORD = 50
# # point_1.MAX_COORD = 150
# # print(point_1.MIN_COORD)
# # print(point_1.MAX_COORD)
# #
# # point_2 = Point(2, 2)
# # print(point_2.MIN_COORD)
# # print(point_2.MAX_COORD)
#
# # point_1 = Point(1, 1)
# # point_1.set_coordinates(1, 50)
# # print(point_1)
# # print(Point.__dict__)
# point = Point(1, 2)
# # point.set_square(40, 80)
# # print(Point.__dict__)
# # point.k = 5
# print(point.y)


class Emoloyee:
    ID = 0
    TAX = 0.13
    STATE = 10000

    def __init__(self, email, salary):
        Emoloyee.ID += 1
        self.id = Emoloyee.ID
        self.email = email
        self.salary = salary

    def get_salary_for_mouth(self, bonus=0):
        return self.salary - self.salary * self.TAX + bonus

    def __str__(self):
        return f"id: {self.id}, email: {self.email}, salary: {self.salary}"


class Manager(Emoloyee):  # Наследование класа
    TAX = 0.1

    def __init__(self, email, salary, employees):
        super(Manager, self).__init__(email, salary)  # Переопределение параметров
        self.employees = employees

    def get_employees(self):
        if self.employees:
            for i_imployees in self.employees:
                print(
                    f"id: {i_imployees.id}\nemail: {i_imployees.email}\nsalary: {i_imployees.salary}"
                )

    def __str__(self):
        return f"id: {self.id}, email: {self.email}, salary: {self.salary}, employees: {self.employees[0]}"


class Enginer(Emoloyee):
    TAX = 0.11

    @classmethod
    def set_state(cls, STATE):
        cls.STATE = STATE

    def __init__(self, email, rank):
        super(Enginer, self).__init__(email, salary=0)
        self.rank = rank

    def get_salary_for_mouth(self, hours=0):
        return Enginer.STATE * hours - Enginer.STATE * hours * self.TAX

    def __str__(self):
        return f"id: {self.id}, email: {self.email}, salary: {self.salary}, rank: {self.rank}"


employee_1 = Emoloyee("test@mail.ru", 10000)
employee_2 = Emoloyee("test_2@mail.ru", 50000)
manager_1 = Manager("boss@mail.ru", 100000, [employee_1])
enginer_1 = Enginer("enginer@mail.ru", 5)
# print(employee_1.get_salary_for_mouth())
# print(employee_2.get_salary_for_mouth())
# print(employee_1)
# print(manager_1)
# print(manager_1.get_salary_for_mouth())
enginer_1.set_state(40000)
print(enginer_1.get_salary_for_mouth(8))
print(enginer_1)
