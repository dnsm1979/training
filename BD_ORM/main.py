from models import *



# new_user = User(username='new_user', email='ychag@example.')
# new_user.save()

# User.create(username='new_user1',age=23, email='ychag1@example.com')
# User.create(username='new_user2',age=20, email='ychag2@example.com')
# User.create(username='new_user3',age=25, email='ychag3@example.com')

# Account.create(nickname='user1', level=11)
# Account.create(nickname='user2', level=15)
# Account.create(nickname='user3', level=20)

# users = User.select()
# for user in users:
#     print(f'{user.username} | {user.email}')

# user = User.get(User.id == 1)
# user.username = 'new_username'
# user.save()
#
# user = User.get(User.id == 1)
# user.delete_instance()
#
# User.delete().where(User.id == 2).execute()


# users = User.select().where(User.username == 'Andrey')
# for user in users:
#     print(f'{user.username} | {user.email}')


# users = User.select().where((User.username == 'Andrey') & (User.age == 23))
# for user in users:
#     print(user.id)

# users = User.select().where((User.username == 'Andrey') | (User.username == 'Aleksey'))
# for user in users:
#     print(user.id)

# users = User.select().where(User.username ** 'A%')
# for user in users:
#     print(user.id)


# users = User.select().where(User.age << [23, 28])
# for user in users:
#     print(user.id)

# users = User.select().where((User.age >= 23) & (User.age <= 28))
# for user in users:
#     print(user.id)


# Product.create(name='APhone', price=100, stock=1)
# Product.create(name='APhone2', price=120, stock=3)
# Product.create(name='aPhone3', price=150, stock=20)

# products = Product.select().where(Product.stock >= 10)
# for product in products:
#     print(f'Название: {product.name}, цена: {product.price}')
#
#
# products = Product.select().where(Product.price >= 200)
# for product in products:
#     print(f'Название: {product.name}, цена: {product.price}')
#
#
# prod = Product.update(price = 110).where(Product.id == 1).execute()
# products = Product.select()
# for product in products:
#     print(f'Название: {product.name}, цена: {product.price}')
#
#
# prod = Product.delete().where(Product.stock == 2).execute()
# products = Product.select()
# for product in products:
#     print(f'Название: {product.name}, цена: {product.price}')
#
#
# products = Product.select().where((Product.price >= 100) & (Product.price <= 150))
# for product in products:
#     print(f'Название: {product.name}, цена: {product.price}')
#
# products = Product.select().where(Product.name ** 'A%')
# for product in products:
#     print(f'Название: {product.name}, цена: {product.price}')
