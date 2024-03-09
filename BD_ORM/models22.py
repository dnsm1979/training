from peewee import *

db = PostgresqlDatabase(
    "peewee", user="postgres", password="root", host="localhost", port="5433"
)


class Department(Model):
    name = CharField()

    class Meta:
        database = db


class Employee(Model):
    name = CharField()
    department = ForeignKeyField(Department, backref="employees")
    salary = DecimalField(max_digits=10, decimal_places=2)
    experience = IntegerField()

    class Meta:
        database = db


if __name__ == "__main__":
    db.create_tables([Department, Employee])
