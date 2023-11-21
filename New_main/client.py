import json
import tkinter as tk
from tkinter import messagebox
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

with open("config.json", "r") as file:
    config = json.load(file)

HOST = config["ip"]
PORT = config["port"]
BUFSIZ = 1024
ADDR = (HOST, PORT)

CLIENT = socket(AF_INET, SOCK_STREAM)
CLIENT.connect(ADDR)


def send(event=None):
    msg = my_msg.get()
    my_msg.set("")
    CLIENT.send(bytes(msg, "utf8"))


root = tk.Tk()
root.title("Bуль буль ")
root.geometry("450x450")

root.option_add("*Font", "{Calibri} 11")
root.option_add("*Background", "pink")

message_frame = tk.Frame(root)
my_msg = tk.StringVar()
scrollbar = tk.Scrollbar(message_frame)


msg_list = tk.Listbox(
    message_frame, height=20, width=60, yscrollcommand=scrollbar.set, background="pink"
)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
message_frame.pack()


entry_field = tk.Entry(root, width=62, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()

send_but = tk.Button(root, text="Отправить", width=15, command=send)
send_but.pack()


def receive():
    while True:
        try:
            msg = CLIENT.recv(BUFSIZ).decode("utf8")
            n = 60
            for i in range(0, len(msg), n):
                msg_list.insert(tk.END, msg[i : (i + n)])
        except OSError:
            break


REEIVE_THREAD = Thread(target=receive)
REEIVE_THREAD.start()

root.mainloop()
