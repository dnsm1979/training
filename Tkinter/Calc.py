import tkinter as tk


root = tk.Tk()
root.title("Простой калькулятор")
icon = tk.PhotoImage(file='icon.png')
root.iconphoto(False, icon)
root.geometry("400x500")
# root.grid_columnconfigure(0, minsize=200)
# root.grid_columnconfigure(1, minsize=200)
# root.grid_rowconfigure(0, minsize=200)
# root.grid_rowconfigure(1, minsize=200)



def get_entry():
    value1 = name.get()
    value2 = name2.get()
    if value1 and value2:
        sum = int(value1) + int(value2)
        # btn['text'] = text=f'{sum}'
        lable = tk.Label(root, text=f'результат: {sum}')
        lable.pack()

    else:
        btn['text'] = f'Некорретный ввод!'

tk.Label(root, text='Число 1').grid(row=0, column=0, stick='w')
name = tk.Entry(root)
name.grid(row=0, column=1)

tk.Label(root, text='Число 2').grid(row=1, column=0, stick='w')
name2 = tk.Entry(root)
name2.grid(row=1, column=1)

btn = tk.Button(root, text='Сложить', command=get_entry)
btn.grid(row=3, column=1, stick='w')



root.mainloop()