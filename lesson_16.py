import random
import time


class Vihicle:
    def __init__(self, name: str, weihgt: float, hp: int, max_speed: int):
        self.name = name
        self.weight = weihgt
        self.hp = hp
        self.wheel_count = 4
        self.refuel = 10
        self.max_speed = max_speed
        self.__possible_failures = ["Дерево", "Столб", "Обрыв"]

    def output_info(self):
        print(
            f"Информация о машине\nназвание: {self.name}\n"
            f"Масса: {self.weight}\n"
            f"hp: {self.hp}"
        )

    def refuel_2(self, litress: float):
        self.refuel += litress
        print(f"Машина заправлена на {self.refuel} литров")

    def refuel_3(self, km):
        self.refuel -= km * 0.1
        if self.refuel <= 0:
            print("Необходимо заправится!")
            choice = int(input("На сколько запрвится?"))
            self.refuel(choice)

        print(f"В баке осталось {self.refuel} литров")

    def boost(self):
        car_time = 0
        for i in range(0, self.max_speed, 20):
            if random.randint(1, 10) == 5:
                print(
                    f"Вы встретили препятствие {random.choice(self.__possible_failures)} при пазгоне"
                )
                return
            car_time += 0.5
            time.sleep(0.5)
            print(f"Текущая скорость: {i} км/ч")
        print(f"Машина {self.name} достигла максимальной скорости!")

    # def __str__(self):
    #     return f'Информация о машине\nназвание: {self.name}\n'f'Масса: {self.weight}\n'f'hp: {self.hp}{self.wheel_count}'


Vihicle_1 = Vihicle(name="audi", weihgt=2000, hp=500, max_speed=250)

# Vihicle_1.output_info()
#
Vihicle_2 = Vihicle(name="bmw", weihgt=1800, hp=520, max_speed=270)

Vihicle_2.output_info()
Vihicle_1.max_speed = 100
print(Vihicle_1.max_speed)
print(Vihicle_1)

Vihicle_1.refuel_2(10)
Vihicle_1.refuel_2(10)
Vihicle_1.refuel_3(150)
Vihicle_1.refuel_3(100)
Vihicle_1.boost()

# class Human:
#     def __init__(self, fulname: str, birth_day: str, tel: str, sity: str, country: str):
#         self.fulname = fulname
#         self.birth_day = birth_day
#         self.tel = tel
#         self.sity = sity
#         self.country = country
#
#     def set_fulname(self, value):
#         self.fulname = value
#
#     def get_fulname(self):
#         return self.fulname
#
# human = Human(fulname='Ivan', birth_day='11.04.2006', tel='799999999', sity='Ekb', country='Ru')
# print(human.get_fulname())
# human.set_fulname('Pitr')
# print(human.get_fulname())
# import random
from typing import List

# class Student:
#     def __init__(self, fulname: str, group_num: str, mark_list: List[int]):
#         self.fulname = fulname
#         self.group_num = group_num
#         self.mark_list = mark_list
#
#     def get_avr_mark(self) -> float:
#         return sum(self.mark_list) / len(self.mark_list)
#
#     def __str__(self):
#         return f'{self.fulname} {self.group_num} {self.get_avr_mark()}'
#
# students = [
#     Student('Ivan', 'P-4', [random.randint(1, 5) for _ in range(5)]),
#     Student('Pitr', 'P-1', [random.randint(1, 5) for _ in range(5)]),
#     Student('Anna', 'P-3', [random.randint(1, 5) for _ in range(5)]),
#     Student('Yula', 'P-1', [random.randint(1, 5) for _ in range(5)]),
#     Student('Vova', 'P-2', [random.randint(1, 5) for _ in range(5)]),
#     Student('Ira', 'P-1', [random.randint(1, 5) for _ in range(5)]),
#     Student('Nona', 'P-2', [random.randint(1, 5) for _ in range(5)]),
#     Student('Michail', 'P-1', [random.randint(1, 5) for _ in range(5)]),
#     Student('Sasha', 'P-3', [random.randint(1, 5) for _ in range(5)]),
#     Student('Soniy', 'P-1', [random.randint(1, 5) for _ in range(5)]),
#
# ]
# sorted_students = sorted(students, key=lambda x: x.get_avr_mark())
#
# for i_student in sorted_students:
#     print(i_student)
