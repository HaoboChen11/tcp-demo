#!/usr/bin/env python3
"""TCP server: receives a message, replies with the same text in uppercase."""

from socket import AF_INET, SOCK_STREAM, socket

SERVER_PORT = 12000


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(("", SERVER_PORT))
    server_socket.listen(1)
    print("The server is ready to receive")

    while True:
        connection_socket, client_address = server_socket.accept()
        with connection_socket:
            message = connection_socket.recv(2048)
            if not message:
                continue

            modified_message = message.decode().upper()
            connection_socket.sendall(modified_message.encode())
            print(f"Received {message} from {client_address}")
            print(f"Sent {modified_message} to {client_address}")


if __name__ == "__main__":
    main()