import socket


def main():
    with socket.create_server(("localhost", 6379), reuse_port=True) as serverSocket:
        connection,address = serverSocket.accept()
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.send(bytes('+PONG\r\n','utf-8'))

if __name__ == "__main__":
    main()
