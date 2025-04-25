from socket import socket, AF_INET, SOCK_STREAM


SERVER_IP="127.0.0.1"
SERVER_PORT=9857

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    s.sendall(b'Hello from client!')