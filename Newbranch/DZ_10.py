# 1 задание
string = input("Введите стоку для проверки: ")
str_2 = string.replace(" ", "")
if str_2.lower() == str_2.lower()[::-1]:
    print("Строка является палиндромом!")
else:
    print("Строка не является палиндромом!")

# 2 задание
# string = input('Введите текст: ').split()
# Words = list(map(str, input('Введите слова через пробел: ').split()))
# sm = set(string)
# print([a for a in sm if a in Words])

# string = input('Введите текст: ')
# Words = input('Введите слово: ')
# print(string.find(Words))
