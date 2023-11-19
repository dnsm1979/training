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
    ...


class Bolognese:
    ...


class Fettuccine_Alfredo:
    ...


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