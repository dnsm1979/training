import re

numbers = input("Введите номера телефонов через пробел: ").split()
t = 0
for i in range(len(numbers)):
    t += 1
    if re.findall(r"\b[89]{1}\d{9}\b", numbers[i]):
        print(f"Номер {t}: всё в порядке!")
    else:
        print(f"Номер {t}: не подходит!")
        print("The end!")
