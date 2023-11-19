class AbstractFactory:
    def create_carbonara(self):
        raise NotImplemented

    def create_bolognese(self):
        raise NotImplemented

    def create_fettuccine_alfredo(self):
        raise NotImplemented



class ConcreteFactory(AbstractFactory):
    def create_carbonara(self):
        return Сarbonara()

    def create_bolognese(self):
        return Bolognese()

    def create_fettuccine_alfredo(self):
        return Fettuccine_Alfredo()


class Сarbonara:
    def __init__(self):
        self.sauce = {}
        self.filling = {}
        self.supplements = {}

    def add_sauce(self, key, value):
        self.sauce[key] = value

    def add_filling(self, key, value):
        self.filling[key] = value

    def add_supplements(self, key, value):
        self.supplements[key] = value

    def __str__(self):
        return f'Pasta Сarbonara from {self.filling} ingredients, with {self.sauce} sauce, with {self.supplements} additives.'


class Bolognese:
    def __init__(self):
        self.sauce = {}
        self.filling = {}
        self.supplements = {}

    def add_sauce(self, key, value):
        self.sauce[key] = value

    def add_filling(self, key, value):
        self.filling[key] = value

    def add_supplements(self, key, value):
        self.supplements[key] = value

    def __str__(self):
        return f'Pasta Bolognese from {self.filling} ingredients, with {self.sauce} sauce, with {self.supplements} additives.'


class Fettuccine_Alfredo:
    def __init__(self):
        self.sauce = {}
        self.filling = {}
        self.supplements = {}

    def add_sauce(self, key, value):
        self.sauce[key] = value

    def add_filling(self, key, value):
        self.filling[key] = value

    def add_supplements(self, key, value):
        self.supplements[key] = value

    def __str__(self):
        return f'Pasta Fettuccine Alfredo from {self.filling} ingredients, with {self.sauce} sauce, with {self.supplements} additives.'

def test_concrete_factory_creation():
    factory = ConcreteFactory()

    assert isinstance(factory, AbstractFactory), "ConcreteFactory is not an instance of AbstractFactory"


def test_product_creation_by_factory():
    factory = ConcreteFactory()

    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    assert isinstance(product_a, ProductA1), "ProductA is not created by ConcreteFactory"
    assert isinstance(product_b, ProductB1), "ProductB is not created by ConcreteFactory"


test_concrete_factory_creation()
test_product_creation_by_factory()