import socket


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        connection,address = server_socket.accept()
        connection.send(bytes('+PONG\r\n','utf-8'))

if __name__ == "__main__":
    main()
