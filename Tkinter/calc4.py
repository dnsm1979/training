import tkinter as tk


root = tk.Tk()
root.title("Простой калькулятор")
icon = tk.PhotoImage(file="icon2.png")
root.iconphoto(False, icon)
root.geometry("400x500")


calc = tk.Entry(root, justify=tk.RIGHT, font=("Arial", 15), width=15)
calc.grid(row=0, column=1, columnspan=5, ipadx=30, ipady=10, padx=5, pady=5, stick="w")


save_opr = []
mem_num = []
oper = []


def save_num():
    save_opr.clear()
    save_opr.append(calc.get())
    insert_btn["background"] = "red"


def add_operation(operation):
    oper.clear()
    oper.append(operation)
    value = calc.get()

    if not mem_num:
        if operation == "*" or operation == "/":
            num = "1"
        else:
            num = "0"
        calc.delete(0, tk.END)
        result = value + operation + num
        calc.insert(0, eval(result))
    else:
        num = mem_num[0]
        calc.delete(0, tk.END)
        result = num + operation + value
        calc.insert(0, eval(result))
    mem_num.clear()
    mem_num.append(calc.get())


def add_digit(digit):
    if not mem_num:
        value = calc.get() + str(digit)
        calc.delete(0, tk.END)
        calc.insert(0, value)
    else:
        if mem_num[0] == calc.get():
            calc.delete(0, tk.END)
        value = calc.get() + str(digit)
        calc.delete(0, tk.END)
        calc.insert(0, value)


def calculate():
    value = calc.get()

    calc.delete(0, tk.END)
    calc.insert(0, eval(value))
    mem_num.clear()
    mem_num.append(calc.get())


def result():
    num = calc.get()
    calc.delete(0, tk.END)
    res = mem_num[0] + oper[0] + num
    calc.insert(0, eval(res))
    mem_num.clear()
    mem_num.append(calc.get())


def make_operation_button(operation):
    return tk.Button(
        text=operation,
        command=lambda: add_operation(operation),
    )


def make_calc_button(operation):
    return tk.Button(text=operation, command=result)


def delete_numbers():
    calc.delete(0, tk.END)
    mem_num.clear()
    oper.clear()


def clear_save_num():
    save_opr.clear()
    # insert_btn['state'] = tk.DISABLED


def sum_save_num():
    if not save_opr:
        save_opr.append(calc.get())
    else:
        so = eval(save_opr[0] + "+" + calc.get())
        save_opr.clear()
        save_opr.append(so)
    # insert_btn['state'] = tk.NORMAL


btn1 = tk.Button(root, text="1", command=lambda: add_digit(1)).grid(
    row=3, column=1, ipadx=15, ipady=10, padx=5, pady=5, stick="w"
)
btn2 = tk.Button(root, text="2", command=lambda: add_digit(2)).grid(
    row=3, column=2, ipadx=15, ipady=10, padx=5, pady=5, stick="w"
)
btn3 = tk.Button(root, text="3", command=lambda: add_digit(3)).grid(
    row=3, column=3, ipadx=15, ipady=10, padx=5, pady=5, stick="w"
)
btn4 = tk.Button(root, text="4", command=lambda: add_digit(4)).grid(
    row=4, column=1, ipadx=15, ipady=10, padx=5, pady=5, stick="w"
)
btn5 = tk.Button(root, text="5", command=lambda: add_digit(5)).grid(
    row=4, column=2, ipadx=15, ipady=10, padx=5, pady=5, stick="w"
)
btn5 = tk.Button(root, text="6", command=lambda: add_digit(6)).grid(
    row=4, column=3, ipadx=15, ipady=10, padx=5, pady=5, stick="w"
)
btn7 = tk.Button(root, text="7", command=lambda: add_digit(7)).grid(
    row=5, column=1, ipadx=15, ipady=10, padx=5, pady=5, stick="w"
)
btn8 = tk.Button(root, text="8", command=lambda: add_digit(8)).grid(
    row=5, column=2, ipadx=15, ipady=10, padx=5, pady=5, stick="w"
)
btn9 = tk.Button(root, text="9", command=lambda: add_digit(9)).grid(
    row=5, column=3, ipadx=15, ipady=10, padx=5, pady=5, stick="w"
)
btn0 = tk.Button(root, text="0", command=lambda: add_digit(0)).grid(
    row=6, column=2, ipadx=15, ipady=10, padx=5, pady=5, stick="w"
)

make_operation_button("+").grid(
    row=6, column=3, columnspan=2, ipadx=43, ipady=10, padx=5, pady=5, stick="w"
)
make_operation_button("-").grid(
    row=5, column=4, ipadx=15, ipady=10, padx=5, pady=5, stick="w"
)
make_operation_button("*").grid(
    row=4, column=4, ipadx=15, ipady=10, padx=5, pady=5, stick="w"
)
make_operation_button("/").grid(
    row=3, column=4, ipadx=15, ipady=10, padx=5, pady=5, stick="w"
)
make_calc_button("=").grid(
    row=7, column=1, columnspan=4, ipadx=103, ipady=10, padx=5, pady=5, stick="w"
)

insert_btn = tk.Button(
    root,
    text="M",
    state="normal",
    command=lambda: add_digit(0) if not save_opr else add_digit(save_opr[0]),
).grid(row=2, column=1, ipadx=12, ipady=5, padx=5, pady=5, stick="w")

sum_btn = tk.Button(root, text="M+", command=sum_save_num).grid(
    row=2, column=2, ipadx=10, ipady=5, padx=5, pady=5, stick="w"
)

cl_save_btn = tk.Button(root, text="M-", command=clear_save_num).grid(
    row=2, column=3, ipadx=10, ipady=5, padx=5, pady=5, stick="w"
)

delete_btn = tk.Button(root, text="C", command=delete_numbers).grid(
    row=2, column=4, ipadx=13, ipady=5, padx=5, pady=5, stick="w"
)
root.mainloop()
