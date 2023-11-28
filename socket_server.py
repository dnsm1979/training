import socket


def start_server():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f"Сервер ожидает на {host}:{port}")

    while True:
        conn, address = server_socket.accept()
        print(f"Соединение установлено с {address}")

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Клиент {data=}")
            message = input("-> ")
            conn.send(message.encode())

        conn.close()
        print("Соединение закрыто")


if __name__ == "__main__":
    start_server()
