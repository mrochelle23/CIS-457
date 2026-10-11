import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 5000

client.connect((host, port))
print(f'Client Connected to server')

clientmessage = input(f'Please type a message')

client.sendall(clientmessage.encode())

storemessage = client.recv(1024).decode()

print(storemessage)

client.close()

print(f'The connection to the server has closed')
