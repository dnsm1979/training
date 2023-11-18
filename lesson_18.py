# class MyZeroDivisionError(ZeroDivisionError):
#
#     def __init__(self, missage=''):
#         self.missage = missage
#
#
#
# def divide(a, b):
#     try:
#         if b == 0:
#             raise MyZeroDivisionError('Деление на ноль!')
#     except MyZeroDivisionError as error:
#         return error.missage
#     # try:
#     #     return a / b
#     # except ZeroDivisionError:
#     #     return f'Деление на ноль!'
#     # except MyZeroDivisionError as error:
#     #     return error.missage
#     # raise MyZeroDivisionError('Деление на ноль!')
# print(divide(10, 0))

# class Vihicle:
#     def __init__(self, weight):
#         self.weight = weight
#
#
# class Ship(Vihicle):
#     pass
#
#
# base_vihicle = Vihicle(1000)
# ship = Ship(1000)
# print(isinstance(ship, Vihicle))  # проверка экземпляра подкласса
# print(issubclass(Ship, Vihicle)) # проверка является ли класс дочерним


# class Multiple:
#     def __init__(self, num_1, num_2):
#         self.num_1 = num_1
#         self.num_2 = num_2
#
#     def __call__(self, *args, **kwargs):
#         print(f'Hi {kwargs["name"]}')
#         return self.num_1 * self.num_2
#
# multiple  =Multiple(10, 15)
# result = multiple(name='Smith')
# print(result)

# Перегрузка операторов


# class Number:
#     def __init__(self, number):
#         self.number = number
#
#     def __add__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number + other.number)
#         else:
#             return 'Сложение не возможно!'
#
#     def __sub__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number - other.number)
#         else:
#             return 'Вычитание не возможно!'
#
#     def __mul__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number * other.number)
#         else:
#             return 'Умножение не возможно!'
#
#     def __truediv__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number / other.number)
#         else:
#             return 'Деление не возможно!'
#
#     def __eq__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number == other.number)
#         else:
#             return 'Сравнение не возможно!'
#
#     def __gt__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number > other.number)
#         else:
#             return 'Сравнение не возможно!'
#
#     def __ge__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number >= other.number)
#         else:
#             return 'Сравнение не возможно!'
#
#     def __lt__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number < other.number)
#         else:
#             return 'Сравнение не возможно!'
#
#     def __le__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number <= other.number)
#         else:
#             return 'Сравнение не возможно!'
#     def __ne__(self, other):
#         if isinstance(other, Number):
#             return Number(self.number != other.number)
#         else:
#             return 'Сравнение не возможно!'
#
# number_1 = Number(10)
# number_2 = Number(11)
# number_3 = Number(12)
# result = number_1 != number_2
# print(result.number)
class Shop:
    def __init__(self, shop_name, adress, tel):
        self.shop_name = shop_name
        self.adress = adress
        self.tel = tel


class Product:
    def __init__(self, name, price, quantity, shop_name, discount=0.0):
        self.shop_name = shop_name
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount

    def get_total_product_price(self):
        return self.price * self.quantity * (1 - self.discount)


class Cart:
    def __init__(self):
        self.cart = []

    def __add__(self, other):
        if isinstance(other, Cart):
            # merge_cart = Cart()
            # merge_cart.cart = self.cart + other.cart
            # return merge_cart
            self.cart += other.cart
            return self
        return "Невозможно произвести слияние карзин!"

    def add_product(self, *args):
        for i_prroduct in args:
            self.cart.append(i_prroduct)

    def get_all_product_in_cart(self):
        print("Товары в корзине:")
        for i_product in self.cart:
            print(
                f"Название: {i_product.name} Цена: {i_product.price} Количество: {i_product.quantity} Магазин: {i_product.shop_name.shop_name} Общая стоимость: {i_product.get_total_product_price()}"
            )
        print(f"Общая стоимость товаров в корзине: {self.get_total_product_amount()}")

    def get_total_product_amount(self):
        total_price = sum(
            [i_product.get_total_product_price() for i_product in self.cart]
        )
        return total_price


shop_1 = Shop("OZON", "12345", "12345")
shop_2 = Shop("OPPO", "54321", "54321")
cart_1 = Cart()
cart_1.add_product(
    Product("apple", 100, 5, shop_1, 0.3), Product("Fish", 500, 2, shop_2)
)
cart_1.get_all_product_in_cart()

cart_2 = Cart()
cart_2.add_product(
    Product("Banana", 100, 5, shop_1), Product("snake", 1500, 2, shop_2, 0.2)
)
cart_2.get_all_product_in_cart()

# cart_3 = cart_1 + cart_2
# cart_3.get_all_product_in_cart()
cart_1 += cart_2
del cart_2
cart_1.get_all_product_in_cart()
