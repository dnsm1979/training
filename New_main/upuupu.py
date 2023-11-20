import json
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

with open('config.json', 'r') as file:
    config = json.load(file)

clients = {}
addresses = {}
users_count = 0

HOST = config['ip']
PORT = config['port']
BUFSIZ = 1024
ADDER = (HOST, PORT)



SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDER)

def handle_client(client):
    global users_count
    users_count += 1
    welcome = f'user {users_count}Салам!'
    client.send(bytes(welcome, 'utf8'))
    msg = f'user{users_count}вошел в чат чат чат чат'
    broadcast(bytes(msg, 'utf8'))
    client[client] = f'user {users_count}'


    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes(f'{quit}', 'utf8'):
            broadcast(msg, f'user {users_count}:')
        else:
            client.close()
            del clients[client]
            broadcast(bytes(f'user{users_count} покинул чат', 'utf8'))
            break
def broadcast(msg, prefix=''):
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)




def get_new():
    while True:
        client, client_address = SERVER.accept()
        print(f'{client_address} ура победа!')
        client.send(bytes(str(client_address) + 'подключился!!!', 'utf8'))

        addresses[client] = client_address
        Thread(target=handle_client, args=(client, )).start()






if __name__ == '__main__':
    SERVER.listen(5)
    print('дем подключения :)')
    ACCEPT_THREAD = Thread(target=get_new)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()

