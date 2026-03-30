import socket
import threading
import json
import os
from dotenv import load_dotenv

load_dotenv()

ip = os.getenv("SERVER_IP")
port = int(os.getenv("SERVER_PORT"))
key = os.getenv("SECRET_KEY")
active_clients = {}

with open("user_database.json", "r",encoding="utf-8") as f:
    user_database = json.load(f)

def is_existing_client(client_id):
    if client_id in user_database:
        return True
    else:
        return False

def new_client_id(client_id, name):

    new_user = {"user_name": name}
    user_database[client_id] = new_user
    with open("user_database.json", "w", encoding="utf-8") as f:
        json.dump(user_database, f)

def handle_client(client_socket, client_address):        
        client_key = client_socket.recv(1024).decode()
        if client_key == key:
            client_socket.send("ack".encode())
            client_id = client_socket.recv(1024).decode()
            if is_existing_client(client_id):
                client_socket.send(user_database[client_id]["user_name"].encode())
                client_name = user_database[client_id]["user_name"]
            else:
                client_socket.send("new client".encode())
                client_name = client_socket.recv(1024).decode()
                new_client_id(client_id, client_name)  
            active_clients[client_id] = [client_socket, client_address, client_name]            
            source_client = active_clients[client_id]
            
            while True:                
                destination_id = source_client[0].recv(1024).decode()
                if destination_id == "??":
                    active_clients_text = ""
                    for client in active_clients:
                        active_clients_text += f"{client, active_clients[client][2]}\n"
                    source_client[0].send(active_clients_text.encode())    
                    continue
                if not destination_id:
                    break
                message = source_client[0].recv(1024).decode()
                if not message:
                    break

                if destination_id in active_clients:
                    active_clients[destination_id][0].send(f"Message from {client_id}, {source_client[2]}: {message}".encode())
                    source_client[0].send("ack".encode())
                else:
                    source_client[0].send("client is not active".encode())
                                        
            active_clients.pop(client_id)
            client_socket.close()
        else:
            client_socket.send("wrong key".encode())
            client_socket.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((ip, port))
    server_socket.listen()    
    print(f"server is listening to {ip}:{port}...")
        
    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
