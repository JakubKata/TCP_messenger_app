import socket
import threading
import os
import time
from dotenv import load_dotenv

load_dotenv()
ip = os.getenv("SERVER_IP")
port = int(os.getenv("SERVER_PORT"))
key = os.getenv("SECRET_KEY")

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        if message == "ack":
            print("Message sent successfully.")
        elif message == "client is not active":
            print("The destination client is not active.")
        else:    
            print(message)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((ip, port))

    client_socket.send(key.encode())
    if "ack" ==client_socket.recv(1024).decode():
        client_id = input("Enter your client ID: ")
        client_socket.send(client_id.encode())
        response = client_socket.recv(1024).decode()
        if response == "new client":
            name = input("Enter your name: ")
            client_socket.send(name.encode())
        else:
            print(f"Welcome back, {response}!")
        
        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

        while True:
            destination_id = input("Enter the destination client ID (or '??' to see active clients): ")
            client_socket.send(destination_id.encode())
            if destination_id == "??":
                time.sleep(1)
                continue
            message = input("Enter your message: ")
            client_socket.send(message.encode())
        
            

