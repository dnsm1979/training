from threading import Thread
import shutil
from os import path


class AllThread:
    def __init__(self):
<<<<<<< HEAD
        self.copy_path = input('Введите путь к исходному каталогу: ')
        self.target_path =input('Введите пить к каталогу для переноса дириктории: ')

=======
        self.copy_path = input("Введите путь к исходному каталогу: ")
        self.target_path = input("Введите пить к каталогу для переноса дириктории: ")
>>>>>>> a411faf1cba4545f4d8e29aff58fedcec0c28c5c

    def copy_dirictory(self):
        source_path = self.copy_path
        if path.exists(source_path):
            destination_path = self.target_path
            new_location = shutil.move(source_path, destination_path)
            print(f"Все файлы и папки перемещаются в нужное место, {new_location}")
        else:
            print("Неверный путь к каталогу.")


if __name__ == "__main__":
    thread = AllThread()
    thread_1 = Thread(target=thread.copy_dirictory())

    print("Поток стартует!")
    thread_1.start()
    print("Поток завершил работу!")
    thread_1.join()

# C:\Users\dnsm1\AppData\Local\Programs\Python\Python39\python.exe C:\Users\dnsm1\PycharmProjects\training\DZ_30_3.py
# Введите путь к исходному каталогу: E:\1
# Введите пить к каталогу для переноса дириктории: E:\2
# Все файлы и папки перемещаются в нужное место, E:\2\1
# Поток стартует!
# Поток завершил работу!
#
# Process finished with exit code 0
