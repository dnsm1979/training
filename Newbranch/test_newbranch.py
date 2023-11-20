string = input("Введите стоку для проверки: ")
str_2 = string.replace(" ", "")
if str_2.lower() == str_2.lower()[::-1]:
    print("Строка является палиндромом!")
else:
    print("Строка не является палиндромом!")
