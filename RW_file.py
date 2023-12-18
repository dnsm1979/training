import shutil

with open("D:\\\\1\\2loran.txt", "r", encoding="utf8") as file_read, open(
    "finish_text.txt", "w", encoding="utf8"
) as file_write:
    shutil.copyfileobj(file_read, file_write)
