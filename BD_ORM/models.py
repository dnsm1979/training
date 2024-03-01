from peewee import *

db = SqliteDatabase('15.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = PrimaryKeyField(unique=True)
    username = CharField(unique=True)
    age = IntegerField()
    email = CharField(unique=True)
    class Meta:
        db_table = 'Users'

class Account(BaseModel):
    id = PrimaryKeyField()
    nickname = CharField(unique=True)
    level = IntegerField()

    class Meta:
        db_table = 'Accounts'

class Product(BaseModel):
    id = PrimaryKeyField()
    name = CharField(unique=True)
    price = IntegerField()
    stock = IntegerField()

    class Meta:
        db_table = 'Products'


if __name__ == '__main__':
    db.create_tables([User, Account, Product])