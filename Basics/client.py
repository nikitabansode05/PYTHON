import socket
import threading

HOST = "192.168.1.81"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to server")


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print(f"\nServer: {message}")

        except:
            break


#thread = threading.Thread(target=receive_messages)
#thread.start()

while True:
    message = input("You: ")
    print(f"You: {message}")
    if message.lower() == "exit":
        client.send("exit".encode())
        break

    client.send(message.encode())

client.close()