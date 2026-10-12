import socket
import threading

# establish client, host and port
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 5008
user = input(f"Please input a username")
connect_message = f"{user} has connected to the server"

# establish connection to server
client.connect((host, port))
client.sendall(connect_message.encode())
print(f"Client Connected to server")

# Send message to server
def send_messages():
    while True:
        clientmessage = f"{user}: {input(f"Please type a message: ")}"
        client.sendall(clientmessage.encode())

# Receive response from server and display to user
def receive_message():
    while True:
        server_message = client.recv(1024).decode()
        print(server_message)

#create and run threads
threads = [threading.Thread(send_messages()), threading.Thread(receive_message())]

for i in threads:
    i.start()

# Close connection with server
# client.close()
# print(f"The connection to the server has closed")
