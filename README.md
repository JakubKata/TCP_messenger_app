# Project Messenger

Project Messenger is a simple, secure client–server messenger written in Python. It uses TLS (SSL) for transport security and RSA for end-to-end message encryption between clients. The repository contains a server and a client application with a lightweight GUI.

Examples of supported scenarios:

- User registration and login
- Active / full clients lists
- Sending encrypted messages between clients
- Offline message storage and delivery when the recipient reconnects
- Server verification using a shared secret key (`SECRET_KEY`)

---

## Features

- TLS-encrypted TCP connections (via Python `ssl`)
- Asymmetric message encryption with RSA
- Support for new-client registration and existing-client login
- Offline message storage (SQLite)
- Simple client GUI using `PySide6`
- Public-key exchange and storage in server database

---

## Requirements

- Python 3.8 or newer
- Virtual environment (recommended)
- Optional dependencies: `PySide6`, `rsa`, `python-dotenv`
- OpenSSL (to generate server certificates)

The project is licensed under the MIT License (see `LICENSE`).

---

## Quick Start (Windows / Linux)

1. Create and activate a virtual environment:

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies (if a `requirements.txt` is present):

```bash
pip install -r requirements.txt
```

3. If needed, install the GUI and crypto packages:

```bash
pip install PySide6 rsa python-dotenv
```

4. Generate a self-signed TLS certificate for the server (example):

```bash
openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes
```

5. Configure environment variables in a `.env` file: `SERVER_IP`, `SERVER_PORT`, `SECRET_KEY`.

---

## Run

Start the server:

```bash
python server/server.py
```

Start the client GUI:

```bash
python client/app.py
```

There are additional client utilities in the `client/` folder for testing and development.

---

## Usage (brief)

1. Run the server on the host defined in `.env`.
2. Start the client, register or log in.
3. Select a recipient and send a message — the server will forward the encrypted payload or store it for offline delivery.

---

## Project Structure

```text
Project_messenger/
├── LICENSE
├── README.md
├── client/
│   ├── app.py
│   ├── client.py
│   ├── protocol.py
│   ├── ui_chat.py
│   └── chat_gui.ui
├── server/
│   ├── server.py
│   ├── protocol.py
│   ├── database.py
│   └── generate_cert.py
└── .env
```

---

## License

MIT

