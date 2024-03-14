import tkinter as tk

root = tk.Tk()
root.geometry("300x500")
root.title("Виджиты")


# def toggle():
#     if toggle_var.get() == 'Вкл':
#         print('On')
#     else:
#         print('Off')
#
# toggle_var = tk.IntVar
# toggle_var.set('Выкл')
#
# yes_no = tk.Checkbutton(root, text="Был на предприятии?", variable=toggle_var, command=toggle, offvalue='Выкл', onvalue='Вкл')
# adv = tk.Checkbutton(root, text="Хочешь получать рекламу?")
# sub = tk.Checkbutton(root, text="Хочешь подписаться на новости?")
# yes_no.pack()
# adv.pack()
# sub.pack()
#
# def select_all():
#     for check in [yes_no, adv, sub]:
#         check.select()
#
# def clear_all():
#     for check in [yes_no, adv, sub]:
#         check.deselect()
#
#
#
#
# tk.Button(root, text="Выбрать все", command=select_all()).pack()
# tk.Button(root, text="Снять все", command=clear_all).pack()


level_var = tk.StringVar()
level_var.set("Новичек")

def submit():
    level = level_var.get()
    print(level)


tk.Label(root, text="Выберите свой уровень")
tk.Radiobutton(root, text="Новичек", variable=level_var, value="Новичек", command=submit).pack()
tk.Radiobutton(root, text="Средний",variable=level_var, value="Средний", command=submit).pack()
tk.Radiobutton(root, text="Профи",variable=level_var, value="Профи", command=submit).pack()


root.mainloop()