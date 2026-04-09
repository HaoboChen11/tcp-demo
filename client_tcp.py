#!/usr/bin/env python3
"""TCP client: sends one message to the server and prints the reply."""

import argparse
from socket import AF_INET, SOCK_STREAM, socket

SERVER_PORT = 12000
DEFAULT_SERVER = "localhost"
DEFAULT_MESSAGE = "hello tcp"


def main():
    parser = argparse.ArgumentParser(description="Send one TCP message to the server and print the reply.")
    parser.add_argument(
        "-s",
        "--server",
        default=DEFAULT_SERVER,
        help=f"Server hostname or IP (default: {DEFAULT_SERVER!r})",
    )
    parser.add_argument(
        "-m",
        "--message",
        default=DEFAULT_MESSAGE,
        help=f"Message to send (default: {DEFAULT_MESSAGE!r})",
    )
    args = parser.parse_args()

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((args.server, SERVER_PORT))
    print(f"Server address: {args.server}:{SERVER_PORT}")
    print(f"Sent {args.message} to server")
    client_socket.sendall(args.message.encode())
    modified_message = client_socket.recv(2048)
    print(f"Received {modified_message.decode()} from server")
    client_socket.close()


if __name__ == "__main__":
    main()