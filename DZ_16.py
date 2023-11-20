db_workers = {}


def add_worker() -> None:
    try:
        contact = input(
            "Введите данные работника через пробел\n"
            " (тел. ФИО email должность кабинет Skype) -> "
        )
        key_ls = (
            phone,
            l_name,
            f_name,
            surname,
            email,
            job,
            cabinet,
            skype,
        ) = contact.split(" ")
    except UnboundLocalError:
        print("Неверный формат ввода!\n")
        main()
    except ValueError:
        print("Неверный формат ввода!\n")
        main()
    vel_ls = [
        "Фамилия",
        "Имя",
        "Отчество",
        "рабочий EMAIL",
        "должность",
        "номер кабинета",
        "Skype",
    ]
    if phone not in db_workers.keys():
        db_workers.setdefault(phone, {})
        key_ls.pop(0)
        db_workers[phone] = dict(zip(vel_ls, key_ls))
        print("\n")
        print(f"Работник {phone} внесен в базу!\n")
    else:
        print("\n")
        print("Работник с таким номером уже есть!\n")


def show_worker() -> None:
    phone = input("Введите телефон работника -> ")
    if phone in db_workers.keys():
        print("\n")
        print(f"Номер телефона: {phone}")
        for i, j in db_workers[phone].items():
            print(i, ":", j)
        print("\n")
    else:
        print("\n")
        print("Такого работника нет!\n")


def del_worker() -> None:
    phone = input("Введите телефон работника -> ")
    print("\n")
    if phone in db_workers.keys():
        chouce = input("Вы действительно хотите удалить данные о работнике? (y/n) -> ")
        if chouce.lower() == "y":
            db_workers.pop(phone)
            print("\n")
            print(f"Информация о работнике {phone} удалена!\n")
        elif chouce.lower() == "n":
            main()
        else:
            print("Не верный фомат ввода!\n")
    else:
        print("Такого контакта нет!\n")


def re_worker() -> None:
    phone = input("Введите телефон работника -> ")
    print("\n")
    if phone in db_workers.keys():
        choice = input(
            "Выберете такую информацию о работнике вы хотите изменить:\n"
            "1-Фамилию, 2-Имя, 3-Отчество, 4-рабочий EMAIL, 5-должность, 6-номер кабинета, 7-Skype ->  "
        )
        print("\n")
        if choice == "1":
            fm = input("Введите новую фамилию: ")
            db_workers[phone]["Фамилия"] = fm
            print(f"Изменения работника {phone} сохранены!\n")
        elif choice == "2":
            nm = input("Введите новое имя: ")
            db_workers[phone]["Имя"] = nm
            print(f"Изменения работника {phone} сохранены!\n")
        elif choice == "3":
            sm = input("Введите новое отчество: ")
            db_workers[phone]["Отчетство"] = sm
            print(f"Изменения работника {phone} сохранены\n!")
        elif choice == "4":
            ml = input("Введите новый рабочий EMAIL: ")
            db_workers[phone]["рабочий EMAIL"] = ml
            print(f"Изменения работника {phone} сохранены!\n")
        elif choice == "5":
            dl = input("Введите новую должность: ")
            db_workers[phone]["должность"] = dl
            print(f"Изменения работника {phone} сохранены!\n")
        elif choice == "6":
            nc = input("Введите новый номер кабинета: ")
            db_workers[phone]["номер кабинета"] = nc
            print(f"Изменения работника {phone} сохранены!\n")
        elif choice == "7":
            sk = input("Введите новый Skype: ")
            db_workers[phone]["Skype"] = sk
            print(f"Изменения работника {phone} сохранены!\n")
    else:
        print("Такого работника нет!")


def main() -> None:
    while True:
        choice = input(
            "1-Добавить работника\n"
            "2-Показать информацию о работнике\n"
            "3-Удалить информацию о работнике\n"
            "4-Редактирование данных работника\n"
            " ->"
        )
        if choice == "1":
            add_worker()
        elif choice == "2":
            show_worker()
        elif choice == "3":
            del_worker()
        elif choice == "4":
            re_worker()
        else:
            print("Такого пункта меню нет!")


main()
