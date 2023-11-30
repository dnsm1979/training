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

    def search_words(self):
        words = []
        with open('finish_text.txt', 'a', encoding="utf-8") as text:
            for w in words:
                for line in text:
                    if w in line:
                        line.replace(w, "")
        with open('finish_text.txt', 'w', encoding="utf-8") as text2:
            text2.write(text)



if __name__ == "__main__":
    thread = AllThread()
    thread_1 = Thread(target=thread.search_file())
    thread_2 = Thread(target=thread.search_words())

    print('Поток стартует!')
    thread_1.start()
    print('Поток завершил работу!')
    thread_1.join()
    print('Поток стартует!')
    thread_2.start()
    print('Поток завершил работу!')
    thread_2.join()