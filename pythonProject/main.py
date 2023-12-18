# file = open('text.txt', 'r')
# text = file.readlines(2)
# print(text)
#
# file.close()

# with open('text.txt', 'r') as file:
#     file.seek(5)
#     print(file.tell())
#     text = file.read()
#     print(text)

# with open('text.txt', 'r') as file:
#     # file.writelines(['Bye\n', 'Bye\n'])
#     for line in file.readlines():
#         print(line.strip() + '$')

# import os
#
# os.rename('text.txt', 'text2.txt')

# import json
#
# human = {'name': 'Иван', 'surname':'Иванов', 'sity':'Москва'}
#
# with open('human.json', 'и') as file:
#     file.write(json.dumps(human))
# with open('human.json', 'r') as file:
#     info = json.loads(file.read())
#     print(info)
import csv

# filename = 'products.csv'
#
# shop_list ={'огурец': [2,100]
#
# with open(filename,'m') as file:
#    writer = csv.writer(file,quoting=csv.QUOTE_ALL)
#    writer.writerow({'Название','Вес/кг', 'Цена/кг'})
#    for name, valves in shop_list.iteans():
#        writer.writerow([name, valves[0], valves(0)))
# import pickle
#
# shop_list = {'огурец': [2,100], 'яблоко': [8,90], 'морковь':[1.3,60]}
#
# with open('shop.txt', 'wb') as file:
#     shop = pickle.load(file)
#     print(shop)

class Car:

    def __init__(self, name, hourse_power, color):
        self.name = name
        self.hourse_power = hourse_power
        self.color = color

    def drive(self):
        print(f'Машина {self.name} едет')

car_1 = Car('Audi', 200,'Красный')
print(car_1.name)
car_1.drive()

car_2 = Car('Lada',80,'синий')
car_2.drive()
