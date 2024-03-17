import tkinter as tk
import math

root = tk.Tk()
root.geometry("400x500")
root.title("Вычисление площади фигур")


level_var = tk.StringVar()
level_var.set(None)


def cleanup():
    for widget in root.winfo_children():

        if isinstance(widget, tk.Label):
            widget.pack_forget()
        if isinstance(widget, tk.Entry):
            widget.pack_forget()
        if isinstance(widget, tk.Button):
            widget.pack_forget()


def squard():
    h = s_entry_1.get()
    print(h)
    print(eval(h + "**" + "2"))
    tk.Label(root, text=eval(h + "**" + "2")).pack()


def triangle():
    a = s_entry_2.get()
    h = s_entry_3.get()
    print(h)
    print(eval("0.5" + a + "*" + h))
    tk.Label(root, text=eval("0.5" + a + "*" + h)).pack()


def circle():
    r = s_entry_4.get()
    print(r)
    print(eval("math.pi" + "*" + r + "**" + "2"))
    tk.Label(root, text=eval("math.pi" + "*" + r + "**" + "2")).pack()


def submit():
    level = level_var.get()
    if level == "Квадрат":
        cleanup()
        tk.Label(root, text=" Размер стороны квадрата:").pack()
        global s_entry_1
        s_entry_1 = tk.Entry(root)
        s_entry_1.pack()

        tk.Button(root, text="Рассчитать", command=squard).pack()

    if level == "Треугольник":
        cleanup()
        tk.Label(root, text=" Размер стороны треугольника:").pack()
        global s_entry_2
        s_entry_2 = tk.Entry(root)
        s_entry_2.pack()
        tk.Label(root, text=" Размер высоты треугольника:").pack()
        global s_entry_3
        s_entry_3 = tk.Entry(root)
        s_entry_3.pack()
        tk.Button(root, text="Рассчитать", command=triangle).pack()

    if level == "Круг":
        cleanup()
        tk.Label(root, text=" Размер радиуса круга:").pack()
        global s_entry_4
        s_entry_4 = tk.Entry(root)
        s_entry_4.pack()
        tk.Button(root, text="Рассчитать", command=circle).pack()


tk.Label(root, text="Выберете фигуру").pack()
tk.Radiobutton(
    root, text="Квадрат", variable=level_var, value="Квадрат", command=submit
).pack()
tk.Radiobutton(
    root, text="Треугольник", variable=level_var, value="Треугольник", command=submit
).pack()
tk.Radiobutton(
    root, text="Круг", variable=level_var, value="Круг", command=submit
).pack()


root.mainloop()
