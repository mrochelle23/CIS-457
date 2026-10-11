import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 5008

client.connect((host, port))
print(f"Client Connected to server")

clientmessage = input(f"Please type a message: ")
client.sendall(clientmessage.encode())

server_message = client.recv(1024).decode()
print("Message from server: ", server_message)

client.close()

print(f"The connection to the server has closed")
