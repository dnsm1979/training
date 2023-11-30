from threading import Thread
import shutil, fnmatch, os

class AllThread:
    def __init__(self):
        self.target_path = input('Введите путь к исходному каталогу: ')
        self.target_world =input('Введите слово для поиска: ')

    def search_file(self):
        word = self.target_world
        for root, dirs, files in os.walk(self.target_path):
            for file in files:
                if file in fnmatch.filter(files, f"*{word}*"):
                    with open((os.path.join(root,file)),'a', encoding="utf-8") as text:
                        # list_text = text.read()
                        with open('finish_text.txt', 'wa', encoding="utf-8") as text_2:
                            text_2.write(f'{text}\n')







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