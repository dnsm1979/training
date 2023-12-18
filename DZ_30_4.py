from threading import Thread
import shutil, fnmatch, os, fileinput, pathlib


class AllThread:
    def __init__(self):
        self.target_path = input("Введите путь к исходному каталогу: ")
        self.target_world = input("Введите слово для поиска: ")

    def search_file(self):
        word = self.target_world
        root = self.target_path
        list_file = []
        for folder, subdirs, files in os.walk(root):
            for filename in fnmatch.filter(files, f"*" + word + "*"):
                fullname = os.path.join(folder, filename)
                list_file.append(fullname)
        print(list_file)
        for file in list_file:
            with open(file, "r", encoding="utf8") as file_read, open(
                "finish_text.txt", "a", encoding="utf8"
            ) as file_write:
                shutil.copyfileobj(file_read, file_write)

        return

    def search_words(self):
        words = ["in", "ut"]
        with open("finish_text.txt", "r", encoding="utf8") as file_read:
            text = file_read.read().split()
            print(text)
            new_text = " ".join((filter(lambda s: s not in words, text)))

            print(new_text)

        with open("finish_text.txt", "w", encoding="utf8") as file_write:
            file_write.write(new_text)


if __name__ == "__main__":
    thread = AllThread()
    thread_1 = Thread(target=thread.search_file())
    thread_2 = Thread(target=thread.search_words())

    print("Поток 1 стартует!")
    thread_1.start()
    print("Поток 1 завершил работу!")
    thread_1.join()
    print("Поток 2 стартует!")
    thread_2.start()
    print("Поток 2 завершил работу!")
    thread_2.join()

# Введите путь к исходному каталогу: D:\1
# Введите слово для поиска: loran
# ['D:\\1\\2loran.txt', 'D:\\1\\loran.txt', 'D:\\1\\loran2.txt']
# Поток 1 стартует!
# Поток 1 завершил работу!
# Поток 2 стартует!
# Поток 2 завершил работу!
