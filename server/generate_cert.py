import os
import subprocess

if not os.path.exists("server.crt") or not os.path.exists("server.key"):
    subprocess.run([
        "openssl", "req", "-x509", "-newkey", "rsa:4096", "-nodes",
        "-out", "server.crt", "-keyout", "server.key", "-days", "365",
    ])
    