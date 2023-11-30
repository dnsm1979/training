import socket


def start_client():
    host = "127.0.0.1"
    port = 12345
    client_cocket = socket.socket()
    client_cocket.connect((host, port))

    message = input("-> ")

    while message.lower().strip() != "quit":
        client_cocket.send(message.encode())
        data = client_cocket.recv(1024).decode()

        print(f"server {data=}")
        message = input("-> ")

    client_cocket.close()


if __name__ == "__main__":
    start_client()
