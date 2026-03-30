import socket
import threading
import os
from dotenv import load_dotenv
from protocol import CMD_MSG, CMD_CLIENTS, CMD_ACK, CMD_NACK, CMD_SAVE, CMD_NEW, CMD_ACTIVE, CMD_ALL

#.env
load_dotenv()
ip = os.getenv("SERVER_IP")
port = int(os.getenv("SERVER_PORT"))
key = os.getenv("SECRET_KEY")

#functions
def receive_messages(client_socket):
    while True:
        data = client_socket.recv(4096).decode()
        if not data:
            break

        messages = data.strip().split("\n")
        for message in messages:
            if not message.strip():
                continue
            parts = message.split("|")
            command = parts[0]
            
            if command == CMD_ACK:
                if parts[1] == CMD_ACK:
                    print("Message sent successfully.")
                elif parts[1] == CMD_SAVE:
                    print("The destination client is offline. The message will be saved and delivered when the client comes online.")
                elif parts[1] == CMD_NACK:
                    print("Failed to send the message. The destination client is not existing.")
            elif command == CMD_MSG:
                print(f"Message from id:{parts[1]} name:{parts[2]}: {parts[3]}")
            else:    
                print(message)

def send_message(client_socket):
    while True:
        destination_id = input("Enter the destination client ID (ALL or 'ACTIVE' to see active clients): ")
        if destination_id == CMD_ACTIVE:
            client_socket.send(f"{CMD_CLIENTS}|{CMD_ACTIVE}\n".encode())
            continue
        if destination_id == CMD_ALL:
            client_socket.send(f"{CMD_CLIENTS}|{CMD_ALL}\n".encode())
            continue
        message = input("Enter your message: ")
        client_socket.send(f"{CMD_MSG}|{destination_id}|{message}\n".encode())
        

def authenticate(client_socket):
    client_socket.send(f"{key}\n".encode())
    authention_response = client_socket.recv(1024).decode().strip()
    if CMD_NACK == authention_response:
        return False
    elif CMD_ACK == authention_response:
        client_id = input("Enter your client ID: ")
        client_socket.send(f"{client_id}\n".encode())
        response = client_socket.recv(1024).decode().strip()

        if response == CMD_NEW:
            name = input("Enter your new name: ")
            password = input("Enter your new password: ")
            client_socket.send(f"{name}|{password}\n".encode())
        else:
            password = input("Enter your password: ")
            client_socket.send(f"{password}\n".encode())
        
        response = client_socket.recv(1024).decode().strip()
        if response.split("|")[0] == CMD_ACK:
            name = response.split("|")[1]
            return True
        else:
            print("Authentication failed.")
            return False
            
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((ip, port))

        if authenticate(client_socket):            
            threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
            send_message(client_socket)
        else:
            client_socket.close()