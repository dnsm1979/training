import operator as op
import tkinter as tk


root = tk.Tk()
root.title("Простой калькулятор")
icon = tk.PhotoImage(file='icon.png')
root.iconphoto(False, icon)
root.geometry("400x500")


def get_entry(oper):
    funcs_names = {
        '+': op.__add__,
        '*': op.__mul__,
        '-': op.__sub__,
        '/': op.truediv
    }
    value1 = name.get()
    value2 = name2.get()
    if value1 and value2:
        result = funcs_names[oper](int(value1), int(value2))
        tk.Label(root, text=f'Результат: {value1} {oper} {value2} = {result}   ').grid(row=4, column=0, stick='e', columnspan=2)
    else:
        tk.Label(root, text=f'Некорретный ввод!').grid(row=4, column=0, stick='e', columnspan=2)

tk.Label(root, text='Число 1').grid(row=0, column=0, stick='w')
name = tk.Entry(root)
name.grid(row=0, column=1)

tk.Label(root, text='Число 2').grid(row=1, column=0, stick='w')
name2 = tk.Entry(root)
name2.grid(row=1, column=1)

tk.Button(root, text='+', command=lambda :get_entry('+')).grid(row=0, column=2, stick='e', rowspan=2, ipadx=6, ipady=6, padx=5, pady=5)
tk.Button(root, text='-', command=lambda :get_entry('-')).grid(row=0, column=3, stick='e', rowspan=2, ipadx=6, ipady=6, padx=5, pady=5)
tk.Button(root, text='*', command=lambda :get_entry('*')).grid(row=0, column=4, stick='e', rowspan=2, ipadx=6, ipady=6, padx=5, pady=5)
tk.Button(root, text='/', command=lambda :get_entry('/')).grid(row=0, column=5, stick='e', rowspan=2, ipadx=6, ipady=6, padx=5, pady=5)
root.mainloop()


