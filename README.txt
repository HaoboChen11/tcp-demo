# TCP socket demo (Python)

The **client** sends one TCP message; the **server** receives it, converts the text to uppercase, and sends a reply.

Find your machine's IP: `ipconfig` (Windows) or `ifconfig` / `ip addr` (Linux/macOS).

## Run (two terminals)

**Terminal 1 - server**

```bash
python server_tcp.py
```

The server listens on all interfaces on port **12000**.

**Terminal 2 - client**

With defaults (`localhost` and a sample message `hello tcp`):

```bash
python client_tcp.py
```

Override server and/or message:

```bash
python client_tcp.py -s 127.0.0.1 -m "my message"
```

To talk to someone else's machine, pass their IP with `-s`.