# TCP socket demo (Python)

The **client** sends one TCP message; the **server** receives it, converts the text to uppercase, and sends a reply.

This repository mirrors the structure and usage of the referenced UDP demo, but uses **TCP** sockets instead.

Find your machine's IP: `ipconfig` (Windows) or `ifconfig` / `ip addr` (Linux/macOS).

## Clone

```bash
git clone https://github.com/HaoboChen11/tcp-demo.git
cd tcp-demo
```

## Files

- `server.py`: TCP server that accepts a connection, reads one message, and replies in uppercase.
- `client.py`: TCP client that connects to the server, sends one message, and prints the reply.

## Run (two terminals)

**Terminal 1 - server**

```bash
python server.py
```

The server listens on all interfaces on port **12000**.

**Terminal 2 - client**

With defaults (`localhost` and a sample message `hello tcp`):

```bash
python client.py
```

Override server and/or message:

```bash
python client.py -s 127.0.0.1 -m "my message"
```

To talk to someone else's machine, pass their IP with `-s`.

## Example output

Server terminal:

```text
The server is ready to receive
Received b'tcp test' from ('127.0.0.1', 64992)
Sent TCP TEST to ('127.0.0.1', 64992)
```

Client terminal:

```text
Server address: localhost:12000
Sent tcp test to server
Received TCP TEST from server
```