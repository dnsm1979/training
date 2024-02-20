from peewee import *


db = SqliteDatabase('Product_data.db')

class BaseModel(Model):
    class Meta:
        database = db

class Product(BaseModel):
    class Meta:
        db_table = 'Products'

    product_id = PrimaryKeyField()
    username = CharField(max_length=100)
    name = CharField(max_length=100)
    price = FloatField()
    description = TextField()

class ProductOwnership(BaseModel):
    class Meta:
        db_table = 'ProductOwnerships'

    ownership_id = PrimaryKeyField()
    user = ForeignKeyField(Product)
    product = ForeignKeyField(Product)
    purchase_data = DateField()


if __name__ == '__main__':
    db.create_tables([Product, ProductOwnership])

