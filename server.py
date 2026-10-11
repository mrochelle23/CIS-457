import socket

# Create the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the server address and port
host = "127.0.0.1"
port = 5008

# Bind the socket and wait for a client connection
server.bind((host, port))
server.listen(1)

print("Server is waiting for a client...")
connection, address = server.accept()
print(f"Connection established with {address}")

# Receive a message from the client
client_message = connection.recv(1024).decode()
print(f"Message from client: {client_message}")

# Type and send a message to the client
server_message = input("Enter a message to send to the client: ")
connection.sendall(server_message.encode())

# Close the connection and the server socket
connection.close()
server.close()

print("Server terminated.")
