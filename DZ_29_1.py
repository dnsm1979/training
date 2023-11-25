class ShoesModel(object):
    def __init__(self, gender, types, color, price, manufacturer, size):
        self.gender = gender
        self.types = types
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size


class ShoesView(object):
    def __init__(self, model):
        self.model = model

    def display_shoes(shoes):
        print(
            f"Gender: {shoes.model.gender}\nType: {shoes.model.types}"
            f"\nColor: {shoes.model.color}\nPrice: {shoes.model.price}"
            f"\nManufacturer: {shoes.model.manufacturer}\nSize: {shoes.model.size}"
        )

    def display_shoes_value(self, value):
        print(f"{value}: {self.model.value}")


class ShoesController(object):
    def __init__(self, model):
        self.model = model
        self.view = ShoesView(self.model)

    def set_shoes(self, value):
        self.model.value = value

    def del_shoes(self, value):
        self.model.value = value
        del self.model.value

    def check_shoes(self, items):
        self.model.values = items
        for i in self.model.value:
            print(i)

            #     print(f"The shoe model {items} is in the database!")
            # else:
            #     print(f"The shoe model {items} is not in the database!")

    def value_shoes(self, value):
        self.view.display_shoes_value(value)

    def display_shoes(self):
        self.view.display_shoes()


if __name__ == "__main__":
    shoes1 = ShoesModel("Man", "Sneakers", "Black", "250$", "Nike", "8.5")
    shoes2 = ShoesModel("Women", "Shoes", "Red", "400$", "Gucсi", "7")

    controller_1 = ShoesController(shoes1)
    controller_1.display_shoes()
    controller_1.value_shoes("7")
