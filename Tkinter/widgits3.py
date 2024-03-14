import tkinter as tk

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

def submit():
    level = level_var.get()
    if level == "Квадрат":
        cleanup()
        L1 = tk.Label(root, text=' Сторона 1:').pack()
        name_entry = tk.Entry(root)
        name_entry.insert(0, " Сторона 1:")
        name_entry.pack()
    if level == "Треугольник":
        cleanup()
        tk.Label(root, text=' Сторона 2:').pack()
        name_entry2 = tk.Entry(root)
        name_entry2.pack()

    if level == "Круг":
        cleanup()
        tk.Label(root, text=' Сторона 3:').pack()
        name_entry3 = tk.Entry(root)
        name_entry3.pack()

tk.Label(root, text='Выберете фигуру').pack()
ch1 = tk.Radiobutton(root, text="Квадрат", variable=level_var, value="Квадрат", command=submit).pack()
ch2 = tk.Radiobutton(root, text="Треугольник", variable=level_var, value="Треугольник", command=submit).pack()
ch3 = tk.Radiobutton(root, text="Круг", variable=level_var, value="Круг", command=submit).pack()

# tk.Label(root, text=' Сторона 1:').pack()
# name_entry = tk.Entry(root)
# name_entry.pack()
# tk.Label(root, text=' Сторона 2:').pack()
# name_entry2 = tk.Entry(root)
# name_entry2.pack()
# tk.Label(root, text=' Сторона 3:').pack()
# name_entry3 = tk.Entry(root)
# name_entry3.pack()

root.mainloop()