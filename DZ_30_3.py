from threading import Thread
import shutil
from os import path

class AllThread:
    def __init__(self):
        self.copy_path = [input('Введите путь к исходному каталогу: ')]
        self.target_path =[input('Введите пить к каталогу для переноса дириктории: ')]


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

    print('Поток стартует!')
    thread_1.start()
    print('Поток завершил работу!')
    thread_1.join()
