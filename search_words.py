words = ["of", "is"]
with open("finish_text.txt", "r", encoding="utf8") as file_read:
    text = file_read.read().split()
    print(text)
    new_text = " ".join((filter(lambda s: s not in words, text)))

    print(new_text)


with open("finish_text.txt", "w", encoding="utf8") as file_write:
    file_write.write(new_text)
