import socket
import threading
import json
import os
from database import init_db, get_client, new_client, offline_message_save, offline_message_read, is_existing_client, get_all_clients
from protocol import CMD_MSG, CMD_CLIENTS, CMD_ACK, CMD_NACK, CMD_SAVE, CMD_NEW, CMD_ACTIVE, CMD_ALL
from dotenv import load_dotenv

#.env
load_dotenv()
ip = os.getenv("SERVER_IP")
port = int(os.getenv("SERVER_PORT"))
key = os.getenv("SECRET_KEY")

#.jsom
with open("config.json", "r",encoding="utf-8") as f:
    config = json.load(f)

init_db()
active_clients = {} #active_client = {client_id : [client_socket, client_address, name, password]}

def get_active_clients():
    active_clients_text = ""
    for id in active_clients:
        active_clients_text += f"{id}, {active_clients[id][2]} |"
    return active_clients_text

def authenticate_key(client_socket, client_address): 
    client_key = client_socket.recv(1024).decode().strip()
    if client_key != key:
        client_socket.send(f"{CMD_NACK}\n".encode())
        client_socket.close()
        return False
    else:
        client_socket.send(f"{CMD_ACK}\n".encode())
        return True
       
def authenticate(client_socket, client_address, client_id):   
    if is_existing_client(client_id):
        client = get_client(client_id)
        active_clients[client_id] = [client_socket, client_address, *client] #active_client = {client_id : [client_socket, client_address, name, password]}
        name = active_clients[client_id][2]
        password = active_clients[client_id][3]
        client_socket.send(f"{CMD_ACK}\n".encode())
        client_password = client_socket.recv(1024).decode().strip()
    else:
        client_socket.send(f"{CMD_NEW}\n".encode())
        response = client_socket.recv(1024).decode().strip()
        if not response or "|" not in response:
            client_socket.close()
            return False
        name, password = response.split("|")
        active_clients[client_id] = [client_socket, client_address, name, password] #active_client = {client_id : [client_socket, client_address, name, password]}
        new_client(client_id, name, password)
        client_password = active_clients[client_id][3]
    
    if password == client_password:
        client_socket.send(f"{CMD_ACK}|{name}\n".encode()) 
        return True
    else:
        client_socket.send(f"{CMD_NACK}\n".encode())
        client_socket.close()
        return False

def handle_client(client_socket, client_address):
    
    if authenticate_key(client_socket, client_address) == False:
        return
    client_id = client_socket.recv(1024).decode().strip()
    if authenticate(client_socket, client_address, client_id) == False:
        return

    offline_data = offline_message_read(client_id)
    if offline_data[0] != None:
        client_socket.send(offline_data[0].encode())

    while True:
        data = client_socket.recv(4096).decode()
        if not data:
            break

        messages = data.split("\n")
        for response in messages:
            if not response.strip(): 
                continue

            parts = response.split("|")
            command = parts[0]
            if command == CMD_CLIENTS:
                if parts[1] == CMD_ACTIVE:
                    clients_text = get_active_clients()
                    client_socket.send(f"{clients_text}\n".encode())
                elif parts[1] == CMD_ALL:
                    clients_text = get_all_clients()
                    client_socket.send(f"{clients_text}\n".encode())
                continue
            if command == CMD_MSG:
                destination_id = parts[1]
                message = parts[2]
                sender_name = active_clients[client_id][2]
                if destination_id in active_clients:
                    active_clients[destination_id][0].send(f"{CMD_MSG}|{client_id}|{sender_name}|{message}\n".encode())
                    client_socket.send(f"{CMD_ACK}|{CMD_ACK}\n".encode())
                else:
                    if is_existing_client(destination_id):
                        client_socket.send(f"{CMD_ACK}|{CMD_SAVE}\n".encode())
                        sender_name = active_clients[client_id][2]
                        offline_message_save(destination_id, client_id, sender_name, message)
                    else:                       
                        client_socket.send(f"{CMD_ACK}|{CMD_NACK}\n".encode())
                        
    active_clients.pop(client_id, None)
    client_socket.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((ip, port))
    server_socket.listen()

    print(f"server is listening to {ip}:{port}...")
        
    while True:
        client_socket, client_address = server_socket.accept()

        if len(active_clients) >= int(config["MAX_CLIENTS"]):
            client_socket.send("server is full".encode())
            client_socket.close()
            continue
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
