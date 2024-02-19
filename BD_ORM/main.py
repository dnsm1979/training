from models import *
def add_product(username, name, price, description):
    Product(
        username=username,
        name=name,
        price=price,
        description=description
    ).save()

def add_product_ownership(user, product, purchase_data):
    ProductOwnership(
        user=user,
        product=product,
        purchase_data=purchase_data
    ).save()
#
# user = User.get(id=1)
# print(user.name)

# users = [x for x in User.select().where(User.money > 1000)]
# for user in users:
#     print(f'{user.tg_id} | {user.name}')

# cust = User.get(id=1)
# exec = User.get(id=2)
#
# Order(
#     custumer=cust,
#     executor=exec,
#     price=400,
#     comment='Нужно провети рекламную компанию'
# ).save()

# executor = User.get(name='Anton')
# orders = [x for x in Order.select().where(Order.executor == executor)]
# print(orders)

if __name__ == '__main__':
    user = ProductOwnership.get(id=2)
    products = [x for x in Product.select()]
    for product in products:
        print(f'{product.product_id} | {product.username} | {user.name} | {product.price} | {product.description}')


    # product = ProductOwnership.get(user='Anton')
    # products = [x for x in Product.select().where(Product.product_id == product)]
    # print(products)

    # add_product('Anton', 'Anton', 1000, 'Anton is a')
    # add_product('Alex', 'Alex', 1500, 'Alex is a')
    # add_product('Pit', 'Pit', 1700, 'Pit is a')
    # add_product_ownership('Anton', 'TOP', 2024-2-19)
    # add_product_ownership('Alex', 'COX', 2024-2-10)
    # add_product_ownership('Pit', 'POT', 2024-2-1)
