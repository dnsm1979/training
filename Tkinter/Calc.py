import tkinter as tk


root = tk.Tk()
root.title("Простой калькулятор")
icon = tk.PhotoImage(file="icon2.png")
root.iconphoto(False, icon)
root.geometry("400x500")
# root.grid_columnconfigure(0, minsize=200)
# root.grid_columnconfigure(1, minsize=200)
# root.grid_rowconfigure(0, minsize=200)
# root.grid_rowconfigure(1, minsize=200)


def get_entry_sum():
    value1 = name.get()
    value2 = name2.get()
    if value1 and value2:
        sum = int(value1) + int(value2)
        tk.Label(root, text=f"результат:{value1}+{value2}={sum}").grid(
            row=4, column=0, stick="w"
        )
    else:
        tk.Label(root, text=f"Некорретный ввод!").grid(row=4, column=0, stick="w")


def get_entry_sub():
    value1 = name.get()
    value2 = name2.get()
    if value1 and value2:
        sub = int(value1) - int(value2)
        tk.Label(root, text=f"результат:{value1}-{value2}={sub}").grid(
            row=4, column=0, stick="w"
        )
    else:
        tk.Label(root, text=f"Некорретный ввод!").grid(row=4, column=0, stick="w")


def get_entry_mult():
    value1 = name.get()
    value2 = name2.get()
    if value1 and value2:
        mult = int(value1) * int(value2)
        tk.Label(root, text=f"результат:{value1}*{value2}={mult}").grid(
            row=4, column=0, stick="w"
        )
    else:
        tk.Label(root, text=f"Некорретный ввод!").grid(row=4, column=0, stick="w")


def get_entry_div():
    value1 = name.get()
    value2 = name2.get()
    if value1 and value2:
        div = int(value1) / int(value2)
        tk.Label(root, text=f"результат:{value1}-{value2}={div}").grid(
            row=4, column=0, stick="w"
        )
    else:
        tk.Label(root, text=f"Некорретный ввод!").grid(row=4, column=0, stick="w")


tk.Label(root, text="Число 1").grid(row=0, column=0, stick="w")
name = tk.Entry(root)
name.grid(row=0, column=1)

tk.Label(root, text="Число 2").grid(row=1, column=0, stick="w")
name2 = tk.Entry(root)
name2.grid(row=1, column=1)

btn = tk.Button(root, text="Сложить", command=get_entry_sum)
btn.grid(row=3, column=1)
btn = tk.Button(root, text="Вычесть", command=get_entry_sub)
btn.grid(row=3, column=2)
btn = tk.Button(root, text="Умножить", command=get_entry_mult)
btn.grid(row=3, column=3)
btn = tk.Button(root, text="Разделить", command=get_entry_div)
btn.grid(row=3, column=4)
root.mainloop()
