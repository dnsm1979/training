class ShoesModel(object):
    def __init__(self, gender, type, color, price, manufacturer, size):
        self.gender = gender
        self.type = type
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size


class ShoesView(object):
    @staticmethod
    def display_shoes(shoes):
        print(f'Gender: {shoes.gender}\nType: {shoes.type}'
              f'\nColor: {shoes.color}\nPrice: {shoes.price}'
              f'\nManufacturer: {shoes.manufacturer}\nSize: {shoes.size}')

class ShoesController(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_shoes_gender(self, values):
        self.model.values = values

    def del_shoes(self, values):
        self.model.values = values
        del self.model.values

    def check_shoes(self, values):
        self.model.values = values
        if values in ShoesModel:
            print(f'The shoe model {values} is in the database!')
        else:
            print(f'The shoe model {values} is not in the database!')

    def number_shoes(self, values):
        self.model.values = values
        count = 0
        for i in self.model.values:
            if i in self.model.values:
                count += 1
        print(f'The number of shoes is in the database {count}')


    def display_shoes(self):
        self.view.display_shoes()


if __name__ == '__main__':
    shoes1 = ShoesModel('Man', 'Sneakers', 'Black', '250$', 'Nike', '8.5')
    shoes2 = ShoesModel('Women', 'Shoes', 'Red', '400$', 'Gucсi', '7')

    controller_1 = ShoesController(shoes1)
    controller_1.display_shoes()