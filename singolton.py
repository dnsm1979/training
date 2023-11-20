class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance


def test_singleton_identify():
    singleton1 = Singleton()
    singleton2 = Singleton()

    assert singleton1 is singleton2  # 'Singlenton instances ara not same'


def test_singleton_state():
    singleton1 = Singleton()
    singleton1.data = "Singleton data"
    singleton2 = Singleton()

    assert singleton2.data == "Singleton data", "Singlenton instances ara not same"


class Logger:
    _instanse = None

    def __new__(cls, output_type="screen"):
        if cls._instanse is None:
            cls._instanse = super(Logger, cls).__new__(cls)
            cls._output_type = output_type

        return cls._instanse

    def log(self, message):
        if self.output_type == "file":
            with open("log.txt", "a") as file:
                file.write(message + "\n")
        else:
            print(message)


def main():
    pach = input("the path to the file: ")
    numbers = int(input("Input numbers: ").split())


file = input("the path to the file: ")
numbers = int(input("numbers: ").split())
