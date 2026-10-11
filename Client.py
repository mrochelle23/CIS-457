import socket

# establish client, host and port
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 5008

# establish connection to server
client.connect((host, port))
print(f"Client Connected to server")

# Send message to server
clientmessage = input(f"Please type a message: ")
client.sendall(clientmessage.encode())

# Receive response from server and display to user
server_message = client.recv(1024).decode()
print("Message from server: ", server_message)

# Close connection with server
client.close()
print(f"The connection to the server has closed")
