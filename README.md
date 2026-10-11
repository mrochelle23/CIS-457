# Simple Python Socket Client-Server App

This project is a minimal Python networking example that demonstrates a basic client/server communication using the `socket` module.

## Overview

The application establishes a TCP connection between:

- `server.py` — waits for an incoming client connection, receives a message, and sends a response back
- `Client.py` — connects to the server, sends a message, and prints the server's response

This project is useful for learning the fundamentals of socket programming in Python, especially local communication on `127.0.0.1`.

## Project Files

- `server.py` — server-side script
- `Client.py` — client-side script

## Requirements

- Python 3.x
- No external libraries required

## How It Works

1. Start the server by running `server.py`.
2. Run `Client.py` in a separate terminal window.
3. The client sends a message to the server.
4. The server receives the message and prompts for a reply.
5. The server sends the reply back to the client.
6. Both sockets close after communication ends.

## Run the Project

### Start the server

```bash
python server.py
```

### Run the client

```bash
python Client.py
```

## Example Flow

- Server starts and waits for a client
- Client connects to `127.0.0.1:5008`
- Client enters a message
- Server prints the message and asks for a response
- Client receives and displays the server response

## Notes

- The server and client communicate over port `5008`.
- Both scripts use the loopback address `127.0.0.1`, which is only available on the local machine.
- This is a simple demonstration and does not include advanced error handling, concurrency, or security protections.
