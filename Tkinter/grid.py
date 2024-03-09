import tkinter as tk


root = tk.Tk()
root.title("Message")
icon = tk.PhotoImage(file="icon2.png")
root.iconphoto(False, icon)
root.geometry("400x500")

# btn1 = tk.Button(root, text='btn1')
# btn2 = tk.Button(root, text='btn2')
# btn3 = tk.Button(root, text='btn3')
# btn4 = tk.Button(root, text='btn4')
# btn5 = tk.Button(root, text='btn5')
# btn6 = tk.Button(root, text='btn6')
# btn7 = tk.Button(root, text='btn7')
# btn8 = tk.Button(root, text='btn8')
#
# btn1.grid(row=0, column=0)
# btn2.grid(row=0, column=1)
# btn3.grid(row=1, column=0)
# btn4.grid(row=1, column=1)
# btn5.grid(row=2, column=0)
# btn6.grid(row=2, column=1)
# btn7.grid(row=3, column=0, columnspan=2, stick='we')
# btn8.grid(row=0, column=2,rowspan=3, stick='ns')

root.grid_columnconfigure(0, minsize=200)
root.grid_columnconfigure(1, minsize=200)
# root.grid_rowconfigure(0, minsize=200)
# root.grid_rowconfigure(1, minsize=200)


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print("No value")


tk.Label(root, text="Имя").grid(row=0, column=1, stick="w")
name = tk.Entry(root)
name.grid(row=0, column=0)

tk.Button(root, text="Send", command=get_entry).grid(row=0, column=2, stick="w")


root.mainloop()
