import tkinter as tk


root = tk.Tk()
root.title("Message")
h = 400
w = 500
root.geometry(f"{h}x{w}")
# root.resizable(True, True)
# root.minsize(200, 400)
icon = tk.PhotoImage(file='icon2.png')
root.iconphoto(False, icon)
# root.config(bg='blue')
lable_1 = tk.Label(root, text='Hello World', bg='pink', fg = 'green',
                   font=('Helvetica','20', 'bold'), padx=10, pady=10, width=10, height=10, anchor='c', relief=tk.RAISED, bd=10)


lable_1.pack()
def button():
    print('Hello')
btn1 = tk.Button(root, text='Click me', command=button)
btn1.pack()

def button2():
    lable = tk.Label(root, text='Heloo!!!!')
    lable.pack()

count = 0

# if count % 2 == 0:
#     btn2 = tk.Button(root, text='Click me2', command=button, state='disabled')
#     btn2.pack()
# else:
#     btn2 = tk.Button(root, text='Click me2', command=button, state='normal')
#     btn2.pack()

btn2 = tk.Button(root, text='Click me2', command=button2, state='normal')
btn2.pack()


def counter():
    global count
    count += 1
    btn3['text'] = text=f'Счетчик {count}'
    if count % 2 == 0:
        btn2['state'] = 'disabled'
    else:
        btn2['state'] = 'normal'

btn3 = tk.Button(root, text=f'Счетчик {count}', command=counter)
btn3.pack()


root.mainloop()