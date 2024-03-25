import tkinter as tk
import math

root = tk.Tk()
root.geometry("400x500")
root.title("Вычисление площади фигур")


level_var = tk.StringVar()
level_var.set(None)

def remove_widgets_based_on_location(master, rows, cols):
    # list widgets to be removed
    widgets = []
    for row in rows:
        for col in cols:
            l = master.grid_slaves(row, col)
            for i in l:
                widgets.append(i)

    # remove widgets
    for widget in widgets:
        # widget.grid_forget()
        widget.pack_forget()
        # widget.place_forget()

def submit():
    level = level_var.get()
    if level == "Квадрат":
        for widget in [ch1, ch2, ch3]:
            widget.pack_forget()
        tk.Label(root, text=" Сторона 1:").pack()

def cleanup():
    for widget in root.winfo_children():

        if isinstance(widget, tk.Label):
            widget.destroy()
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
<<<<<<< HEAD
        tk.Label(root, text=' Сторона 1:').pack()
        name_entry = tk.Entry(root)
        name_entry.pack()
    if level == "Треугольник":
        cleanup()
        tk.Label(root, text=' Сторона 2:').pack()
        name_entry2 = tk.Entry(root)
        name_entry2.pack()

    if level == "Круг":
        remove_widgets_based_on_location(master=root,
                                         rows=[4, 5, 6],
                                         cols=[])
        tk.Label(root, text=' Сторона 3:').pack()
        name_entry3 = tk.Entry(root)
        name_entry3.pack()
=======
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
>>>>>>> c51fad586cf9db8e4c1e11890a0a445a3d94e565


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

<<<<<<< HEAD

# tk.Label(root, text=' Сторона 1:').pack()
# name_entry = tk.Entry(root)
# name_entry.pack()
# tk.Label(root, text=' Сторона 2:').pack()
# name_entry2 = tk.Entry(root)
# name_entry2.pack()
# tk.Label(root, text=' Сторона 3:').pack()
# name_entry3 = tk.Entry(root)
# name_entry3.pack()
=======
>>>>>>> c51fad586cf9db8e4c1e11890a0a445a3d94e565

root.mainloop()
