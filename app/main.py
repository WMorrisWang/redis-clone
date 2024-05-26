import socket
from selectors import DefaultSelector, EVENT_READ

selector = DefaultSelector()


def acceptSocket(serverSocket: socket.socket) -> None:
    connection, _ = serverSocket.accept()
    connection.setblocking(False)
    selector.register(connection, EVENT_READ, readSocket)


def readSocket(connection: socket.socket) -> None:
    data = connection.recv(1024)
    if not data:
        selector.unregister(connection)
        connection.shutdown(socket.SHUT_RDWR)
        connection.close()
        return
    connection.sendall(b"+PONG\r\n")


def main():
    try:
        with socket.create_server(("localhost", 6379), reuse_port=True) as serverSocket:
            serverSocket.setblocking(False)
            selector.register(serverSocket, EVENT_READ, acceptSocket)
            while True:
                for selectKey, _ in selector.select():
                    callback = selectKey.data
                    callback(selectKey.fileobj)
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
