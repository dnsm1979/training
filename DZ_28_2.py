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
        return f"Pasta Сarbonara from {self.filling} ingredients, with {self.sauce} sauce, with {self.supplements} additives."


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
        return f"Pasta Bolognese from {self.filling} ingredients, with {self.sauce} sauce, with {self.supplements} additives."


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
        return f"Pasta Fettuccine Alfredo from {self.filling} ingredients, with {self.sauce} sauce, with {self.supplements} additives."


def test_concrete_factory_creation():
    factory = ConcreteFactory()

    assert isinstance(
        factory, AbstractFactory
    ), "ConcreteFactory is not an instance of AbstractFactory"


def test_product_creation_by_factory():
    factory = ConcreteFactory()

    carbonara = factory.create_carbonara()
    bolognese = factory.create_bolognese()
    fettuccine_alfredo = factory.create_fettuccine_alfredo()

    assert isinstance(
        carbonara, Сarbonara
    ), "ProductA is not created by ConcreteFactory"
    assert isinstance(
        bolognese, Bolognese
    ), "ProductB is not created by ConcreteFactory"
    assert isinstance(
        fettuccine_alfredo, Fettuccine_Alfredo
    ), "ProductB is not created by ConcreteFactory"


test_concrete_factory_creation()
test_product_creation_by_factory()
print(Сarbonara)
