sym_glas = "уеэоаыяию"
sym_soglas = "бвгджзйклмнпрстфхцчшщ"
sym_ost = "ъь"
sym_num = "1234567890"
gl = 0
sg = 0
sn = 0
lines = 0
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()
    symbols = len(text)
    file.seek(0)
    line_num = len(file.readlines())
    with open("score.txt", "w") as file_2:
        for i in text.lower():
            if i in sym_glas:
                gl += 1
            if i in sym_soglas:
                sg += 1
            if i in sym_num:
                sn += 1

        file_2.write(
            f"* Количество символов: {symbols}\n* Количество строк: {line_num}\n* Количество гласных букв: {gl}\n* Количество согласных букв: {sg}\n* Количество цифр: {sn}"
        )
    print(
        f"* Количество символов: {symbols}\n* Количество строк: {line_num}\n* Количество гласных букв: {gl}\n* Количество согласных букв: {sg}\n* Количество цифр: {sn}"
    )
