import socket
import sqlite3
import threading
import json
import os
from dotenv import load_dotenv

#.env
load_dotenv()
ip = os.getenv("SERVER_IP")
port = int(os.getenv("SERVER_PORT"))
key = os.getenv("SECRET_KEY")

#.jsom
with open("config.json", "r",encoding="utf-8") as f:
    config = json.load(f)

#database
def init_db():
    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            client_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            password TEXT NOT NULL,
            offline_messages TEXT
        )""")
    conn.commit()
    conn.close()

init_db()

def get_client(client_id):
    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, password FROM users WHERE client_id = ?", (client_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def new_client(client_id, name, password):
    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (client_id, name, password) VALUES (?, ?, ?)", (client_id, name, password))
    conn.commit()
    conn.close()

def is_existing_client(client_id):
    if get_client(client_id) == None:
        return False
    else:
        return True

def offline_message_read(client_id):
    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()
    cursor.execute("SELECT offline_messages FROM users WHERE client_id = ?", (client_id,))
    result = cursor.fetchone()
    cursor.execute("UPDATE users SET offline_messages = NULL WHERE client_id = ?", (client_id,))
    conn.commit()
    conn.close()
    return result

def offline_message_save(destination_id, client_id, message):
    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()
    cursor.execute("SELECT offline_messages FROM users WHERE client_id = ?", (destination_id,))
    result = cursor.fetchone()
    if result[0] == None:
        new_offline_message = f"MSG|{client_id}|{active_clients[client_id][2]}|{message}\n"
    else:
        new_offline_message = result[0] + f"MSG|{client_id}|{active_clients[client_id][2]}|{message}\n"
    cursor.execute("UPDATE users SET offline_messages = ? WHERE client_id = ?", (new_offline_message, destination_id))
    conn.commit()
    conn.close()

def get_active_clients():
    active_clients_text = ""
    for id in active_clients:
        active_clients_text += f"{id}, {active_clients[id][2]}\n"
    return active_clients_text

def get_all_clients():
    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()
    cursor.execute("SELECT client_id, name FROM users")
    result = cursor.fetchall()
    conn.close()
    all_clients_text = ""
    for r in result:
        all_clients_text += f"{r[0]}, {r[1]}\n"
    return all_clients_text

active_clients = {} #active_client = {client_id : [client_socket, client_address, name, password]}

def handle_client(client_socket, client_address):
    #authentication    
    client_key = client_socket.recv(1024).decode()
    if client_key != key:
        client_socket.send("NACK".encode())
        client_socket.close()
        return
    else:
        client_socket.send("ACK".encode())

    client_id = client_socket.recv(1024).decode()
    if is_existing_client(client_id):
        client = get_client(client_id)
        active_clients[client_id] = [client_socket, client_address, *client] #active_client = {client_id : [client_socket, client_address, name, password]}
        name = active_clients[client_id][2]
        password = active_clients[client_id][3]
        client_socket.send("ACK".encode())
        client_password = client_socket.recv(1024).decode()
    else:
        client_socket.send("NEW".encode())
        response = client_socket.recv(1024).decode()
        name, password = response.split("|")
        active_clients[client_id] = [client_socket, client_address, name, password] #active_client = {client_id : [client_socket, client_address, name, password]}
        new_client(client_id, name, password)
        client_password = active_clients[client_id][3]
    
    if password == client_password:
        client_socket.send(f"ACK|{name}".encode()) 

        #handling
        offline_data = offline_message_read(client_id)
        if offline_data[0] != None:
            client_socket.send(offline_data[0].encode())

        while True:
            response = client_socket.recv(4096).decode()
            if not response:
                break
            parts = response.split("|")
            command = parts[0]
            if command == "CLIENTS":
                if parts[1] == "ACTIVE":
                    clients_text = get_active_clients()
                    client_socket.send(clients_text.encode())
                elif parts[1] == "ALL":
                    clients_text = get_all_clients()
                    client_socket.send(clients_text.encode())
                continue
            if command == "MSG":
                destination_id = parts[1]
                message = parts[2]
                if destination_id in active_clients:
                    active_clients[destination_id][0].send(f"MSG|{client_id}|{active_clients[client_id][2]}|{message}".encode())
                    client_socket.send("ACK|ACK".encode())
                else:
                    if is_existing_client(destination_id):
                        client_socket.send("ACK|SAVE".encode())
                        offline_message_save(destination_id, client_id, message)
                    else:                       
                        client_socket.send("ACK|NACK".encode())
                           
        active_clients.pop(client_id, None)
        client_socket.close()
    else:
        client_socket.send("NACK".encode())
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
