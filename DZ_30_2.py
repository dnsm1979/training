import sys, os
from threading import Thread


class AllThread:
    def __init__(self):
        self.input_number = []
        self.prime_number = []
        self.factorial_number = []

    def load_file(self):
        date_in_file = os.path.join(sys.path[0], "data_thread.txt")
        with open(date_in_file, encoding="utf-8") as f:
            self.input_number = f.read().split()

    def get_prime(self):
        date_in_file = os.path.join(sys.path[0], "prime.txt")
        with open(date_in_file, "w") as f:
            for i in self.input_number:
                if self.isPrime(int(i)):
                    self.prime_number.append(i)
                    f.write(i + "\n")

    def get_factorial(self):
        date_in_file = os.path.join(sys.path[0], "factorial.txt")
        with open(date_in_file, "w") as f:
            for i in self.input_number:
                tmp = self.factorial(int(i))
                self.factorial_number.append(tmp)
                f.write(tmp + "\n")

    def isPrime(self, n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return str(d * d > n)

    def factorial(self, n):
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return str(factorial)


if __name__ == "__main__":
    all_thread = AllThread()

    t1 = Thread(target=all_thread.load_file())
    t2 = Thread(target=all_thread.get_prime())
    t3 = Thread(target=all_thread.get_factorial())

    t1.start()
    t1.join()

    t2.start()
    t3.start()

    print(*all_thread.prime_number, sep=" ,")
    print(*all_thread.factorial_number, sep="\n")
