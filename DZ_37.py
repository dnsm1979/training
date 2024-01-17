import psycopg2


def add_student():
    conn = psycopg2.connect(
        dbname="students", host="localhost", user="postgres", password="1", port="5432"
    )
    cursor = conn.cursor()

    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")

    cursor.execute(
        """INSERT INTO students(FirstName, LastName) VALUES (%s, %s);""",
        (first_name, last_name),
    )
    conn.commit()
    print(f"Студент {first_name} {last_name} добавлен в базу!\n")

    cursor.close()
    conn.close()


def add_grade():
    conn = psycopg2.connect(
        dbname="students", host="localhost", user="postgres", password="1", port="5432"
    )
    cursor = conn.cursor()

    id = int(input("Введите id студента: "))
    subject = input("Введите предмет: ")
    grade = int(input("Введите оценку по предмету: "))

    cursor.execute(
        """INSERT INTO grades(StudentID, Subject, Grade) VALUES (%s, %s, %s);""",
        (id, subject, grade),
    )
    conn.commit()
    print(f"Оценка для предмета {subject} добавлена!\n")

    conn.close()
    cursor.close()


if __name__ == "__main__":
    while True:
        choice = int(
            input(
                "Выберети пункт меню\n"
                "1 - Добавить студента студента\n"
                "2 - Добавить оценку студенту по предмету\n"
                "3 - Выйти из программы  ->>"
            )
        )
        print()
        if choice == 1:
            add_student()
        elif choice == 2:
            add_grade()
        elif choice == 3:
            break
        else:
            print("Некоретный ввод!")
