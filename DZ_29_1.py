class ShoesModel:
    size_dict = {"7": 40, "7.5": 41, "8": 42}

    def __init__(self, gender, types, color, price, manufacturer, size):
        self.gender = gender
        self.types = types
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size


class ShoesView:
    def __init__(self, model):
        self.model = model

    def display_shoes(shoes):
        print(
            f"Gender: {shoes.model.gender}\nType: {shoes.model.types}"
            f"\nColor: {shoes.model.color}\nPrice: {shoes.model.price}"
            f"\nManufacturer: {shoes.model.manufacturer}\nSize: {shoes.model.size}"
        )

    def display_shoes_size_ru(self, value):
        print(f"Ru size shoes: {value}")


class ShoesController:
    def __init__(self, model):
        self.model = model
        self.view = ShoesView(self.model)

    def set_shoes(self, value):
        self.model.value = value

    def display_shoes(self):
        self.view.display_shoes()

    def display_size(self, value):
        size_ru = self.model.size_dict[value]
        self.view.display_shoes_size_ru(size_ru)


if __name__ == "__main__":
    shoes1 = ShoesModel("Man", "Sneakers", "Black", "250$", "Nike", "8.5")
    shoes2 = ShoesModel("Women", "Shoes", "Red", "400$", "Gucсi", "7")

    controller_1 = ShoesController(shoes1)
    controller_1.display_shoes()
    controller_1.display_size("7")
