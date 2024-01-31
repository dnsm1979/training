import psycopg2

conn = psycopg2.connect(
    dbname="data", host="Localhost", user="postgres", password="1", port="5432"
)
conn.autocommit = True


#  #Объект для взаимодействия с бд
# cursor.execute(''' CREATE TABLE users(id serial PRIMARY KEY, first_name varchar NOT NULL, nick_name varchar NOT NULL)''')
# print('Таблица создана!')
# cursor.execute('''INSERT INTO users(first_name,nick_name) VALUES('Oleg', 'OlegTop');''')
# print('Данные дабавлены!')
# cursor.execute(''' DROP TABLE users; ''')
# print('Таблица удалена!')
# cursor.execute(''' SELECT * FROM airports_data; ''')
# print(cursor.fetchall())
# cursor.execute(''' SELECT MODEL FROM AIRCRAFTS_DATA WHERE RANGE > 5000;  ''')
# print(cursor.fetchall())
# cursor.execute(''' SELECT * FROM tickets WHERE PASSENGER_NAME LIKE 'N%'; ''')
# print(cursor.fetchall())
# cursor.execute(''' SELECT * FROM AIRPORTS_DATA WHERE CITY ->> 'ru' = 'Москва'; ''')
# print(cursor.fetchall())
# cursor.execute(''' SELECT * FROM BOOKINGS
#                     JOIN TICKETS ON TICKETS.BOOK_REF = BOOKINGS.BOOK_REF
#                     WHERE TICKETS.PASSENGER_ID = '8149 604011'; ''')
# print(cursor.fetchall())
# cursor.execute(''' SELECT * FROM flights WHERE SCHEDULED_DEPARTURE < ACTUAL_DEPARTURE GROUP BY FLIGHT_ID LIMIT 5; ''')
# print(cursor.fetchall())
# cursor.execute(''' SELECT COUNT(airport_code) AS COUNT_AIRPOTS FROM airports_data; ''')
# print(cursor.fetchall())
cursor = conn.cursor()


def menu():
    choise = int(
        input(
            "Выберете пункт меню! /n"
            "1-Добовление студента /n"
            "2-Добавление оценки /n"
            "3-Выйти из программы -->"
        )
    )
    if choise == 1:
        return add_student()
    elif choise == 2:
        return add_grades()
    elif choise == 3:
        return
    else:
        print("Неверный выбор!")
        return menu()


def add_student():
    name = input("Введите имя:  ")
    surname = input("Введите фамилию:  ")
    cursor.execute(
        "INSERT INTO students(FirstName,LastName) VALUES(%s, %s)", (name, surname)
    )
    print("Данные дабавлены!")


def add_grades():
    id_student = input("Введите id:  ")
    Subject = input("Введите предмет:  ")
    Grade = input("Введите оценку:  ")
    cursor.execute(
        "INSERT INTO grades(Subject,Grade) VALUES(%s, %s) WHERE ID(%s)",
        (Subject, Grade, id_student),
    )
    print("Данные дабавлены!")


conn.close()
cursor.close()


while True:
    menu()
# conn.close()
# cursor.close()
