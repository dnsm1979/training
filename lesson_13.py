
# file = open('filename.txt', 'r') # открытие файла r-чтение, w-запись, a-дозапись, r+ - чтение и запись, w+ -
# file.write(f'Привет, я файл!\n')
# file.write(f'Привет, я файл!\n')
# for i in range(5):
#     file.write('Привет, я файл!\n')
# text = file.read()
# # file.write('Ok')
# print(text)
# try:
#     text = file.readline()
#     raise ValueError
#     print(text)
# except ValueError:
#     print('Error!')
# finally:
#     print('File cloused!')
#     file.close() # закрытие файла

# filename_bin = open('file.bin', 'rb')
# filename_bin.write(bytes('какой то текст!'.encode()))
# print(filename_bin.read())
# filename_bin.close()

# with open('filename.txt', 'r') as file: # Контекстный мененджер, авто закрытие файла
#     print(file.read())

# with open('filename.txt', 'w') as file:
#     file.write('Привет')
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# def ceasar_code(text, shift) -> str:
#     decrypted_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in text.lower()]
#     return ''.join(decrypted_list)
# with open('text.txt', 'w', encoding='utf-8') as file_1:
#     for i in range(5):
#         file_1.write('Привет\n')
# with open('cipher_text.txt', 'a', encoding='utf-8') as file_2:
#     with open('text.txt', 'r', encoding='utf-8') as file_1:
#         lines = file_1.readlines()
#         shift = 1
#         for i_line in lines:
#             ciphered = ceasar_code(i_line.strip(), shift)
#             file_2.write(ciphered + '\n')
#             shift += 1
import random

# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# def ceasar_code(text, shift) -> str:
#     decrypted_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in text.lower()]
#     return ''.join(decrypted_list)
# with open('text.txt', 'w', encoding='utf-8') as file_1:
#     for i in range(5):
#         file_1.write('Привет\n')
# with open('cipher_text.txt', 'a', encoding='utf-8') as file_2:
#     with open('text.txt', 'r', encoding='utf-8') as file_1:
#         lines = file_1.readlines()
#         shift = 1
#         for i_line in lines:
#             ciphered = ceasar_code(i_line.strip(), shift)
#             # file_2.write(ciphered[:len(ciphered) // 2] + f'({shift})' + ciphered[len(ciphered) // 2:] + '\n')
#             ciphereds = ciphered[3:] + str(f'({shift})') + ciphered[:-3]
#             file_2.write(ciphereds + '\n')
#             shift += 1
# frequency = {}
# with open('zen.txt', 'r') as file:
#     text = file.read().lower()
    # for sym in text:
    #     if sym.isalpha():
    #         frequency.setdefault(sym, text.count(sym))
    # frequency = {sym: text.count(sym) for sym in text if sym.isalpha()}
    # print(frequency)
    # alpha_num = len(frequency.keys())
    # total_num = sum(frequency.values())
    # min_alpha = min(frequency.values())
    #
    # max_alpha = max(frequency.values())
    # file.seek(0)
    # line_num = len(file.readlines())
    # world_num = len(text.split())
    # print(alpha_num, total_num, min_alpha, max_alpha, line_num, world_num)

# with open('zen.txt', 'r') as file:
#     text = file.read()
#
#     with open('zen_2.txt', 'w') as file_2:
#         for sym in reversed(text):
#             file_2.write(sym)

with open('zen_3.txt', 'r', encoding='utf-8') as file:

    with open('zen.txt', 'r', encoding='utf-8') as file_2:
        text_2 = file_2.read()
        for bad in file.readlines():
            if bad.strip() in text_2:
                text_2 = text_2.replace(bad, '')
    with open('zen_4.txt', 'w', encoding='utf-8') as file_3:
        file_3.write(text_2)


