from threading import Thread
import shutil, fnmatch, os, fileinput, pathlib

class AllThread:
    def __init__(self):
        self.target_path = input('Введите путь к исходному каталогу: ')
        self.target_world =input('Введите слово для поиска: ')



    def search_file(self):
        word = self.target_world
        for root, dirs, files in os.walk(self.target_path):
            for file in files:
                if file in fnmatch.filter(files, f"*"+word+"*"):
                    with open(os.path.join(root,file),'a') as file_read, open('finish_text.txt', 'w') as file_write:
                        for line in file_read:
                            if file_read.isfirstline():
                                file_name = file_read.filename()
                                file_write.write(f'\n\n------------ {file_name}\n\n')
                            file_write.write(line)

    def search_words(self):
        words = ['is', 'of']
        with open('finish_text.txt', 'a') as file_read, open('finish_text.txt', 'w') as file_write:
            for w in words:
                for line in file_read:
                    if w in line:
                        line.replace(w, "")
                        file_write.write(line)




if __name__ == "__main__":
    thread = AllThread()
    thread_1 = Thread(target=thread.search_file())
    thread_2 = Thread(target=thread.search_words())

    print('Поток 1 стартует!')
    thread_1.start()
    print('Поток 1 завершил работу!')
    thread_1.join()
    print('Поток 2 стартует!')
    thread_2.start()
    print('Поток 2 завершил работу!')
    thread_2.join()