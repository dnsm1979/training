from threading import Thread
from random import randint


class AllThread:
    def __init__(self):
        self.rnd_numbers = []
        self.average = 0
        self.summa = 0

    def rnd(self):
        self.rnd_numbers = [randint(0, 100) for i in range(10)]

    def summ(self):
        self.summa = sum(self.rnd_numbers)

    def avg(self):
        self.average = sum(self.rnd_numbers) / len(self.rnd_numbers)


if __name__ == "__main__":
    all_thread = AllThread()

    t1 = Thread(target=all_thread.rnd())
    t2 = Thread(target=all_thread.summ())
    t3 = Thread(target=all_thread.avg())

    t1.start()
    t1.join()

    t2.start()
    t3.start()

print(*all_thread.rnd_numbers, sep=", ")
print(f"Summa: {all_thread.summa}")
print(f"Average: {all_thread.average}")
