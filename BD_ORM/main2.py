from models import *


def add_product(username, name, price, description):
    Product(username=username, name=name, price=price, description=description).save()


def add_product_ownership(user, product, purchase_data):
    ProductOwnership(user=user, product=product, purchase_data=purchase_data).save()


def show_product():
    print(
        "Катую онформацию получить: \n1-Информаю о всех продуктах\n2-Информацию о конкретном продукте"
    )
    choice = input("Введите выбор: ")
    if choice == "1":
        print(f"Ваш список продуктов:")
        for x in Product:
            print(f" Название: {x.name}, цена: {x.price}, описание: {x.description}")
    elif choice == "2":
        for x in Product:
            if x.name == input("Введите название продукта: "):
                print(f"Название: {x.name}, цена: {x.price}, описание: {x.description}")
            else:
                print("Продукта нет в списке!")
            return
    else:
        print("Не коретный выбор!")
    return


if __name__ == "__main__":

    while True:
        print(
            f"Выберете пункт меню:\n1-Добавить продукт\n2-Добавить информацию о покупке\n3-Получить информацию"
        )
        menu = input("Выберете пункт: ")
        if menu == "1":
            add_product(
                input("Введите имя: "),
                input("Введите название: "),
                input("Введите цену: "),
                input("Введите описание: "),
            )
            print("Продукт добавлен!")
        elif menu == "2":
            add_product_ownership(
                input("Введите имя: "),
                input("Введите название: "),
                input("Введите дату покупки: "),
            )
            print("Информация добавлена!")
        elif menu == "3":
            show_product()

        else:
            print("Не коретный выбор!")

    # add_product('Anton', 'ipad', 1000, 'Планшет')
    # add_product('Alex', 'iPhone Max', 1500, 'Топовый смартфон')
    # add_product('Piter', 'Samsung Fold 5', 1700, 'Раскладной смартфон')
    # add_product_ownership('Anton', 'планшет', '2024-02-19')
    # add_product_ownership('Alex', 'смартфон', '2024-02-10')
    # add_product_ownership('Piter', 'смартфон', '2024-02-01')
