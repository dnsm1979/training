import tkinter as tk

root = tk.Tk()
root.geometry("400x500")
root.title("Виджиты")

tk.Label(root, text="Введите ваше имя:").pack()
name_entry = tk.Entry(root)
name_entry.pack()


tk.Label(root, text="Выберите ваш пол:").pack()
level_var = tk.StringVar()
level_var.set("мужской")


def submit():
    level = level_var.get()


tk.Radiobutton(
    root, text="мужской", variable=level_var, value="мужской", command=submit
).pack()
tk.Radiobutton(
    root, text="женский", variable=level_var, value="женский", command=submit
).pack()

tk.Label(root, text="Выберите ваши любимые языки программирования:").pack()


def show_user():
    name = name_entry.get()
    level = level_var.get()
    print(f"Пользователь: {name},\n Пол: {level}\nЯзыки программирования:")
    if toggle_var1.get() == 1:
        print("Python")
    if toggle_var2.get() == 1:
        print("Java")
    if toggle_var3.get() == 1:
        print("C++")
    if toggle_var4.get() == 1:
        print("C#")


toggle_var1 = tk.IntVar()
toggle_var2 = tk.IntVar()
toggle_var3 = tk.IntVar()
toggle_var4 = tk.IntVar()


tk.Checkbutton(root, text="Python", variable=toggle_var1).pack()
tk.Checkbutton(root, text="Java", variable=toggle_var2).pack()
tk.Checkbutton(root, text="C++", variable=toggle_var3).pack()
tk.Checkbutton(root, text="C#", variable=toggle_var4).pack()


tk.Button(root, text="Отправить", command=show_user).pack()


root.mainloop()
