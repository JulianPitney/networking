from socket import socket, AF_INET, SOCK_STREAM

SERVER_IP="127.0.0.1"
SERVER_PORT=9857
MAX_QUEUED_CONNECTIONS = 10
CLIENT_CONN_BUF_SIZE = 1024


with socket(AF_INET, SOCK_STREAM) as s:

    s.bind((SERVER_IP, SERVER_PORT))
    s.listen(MAX_QUEUED_CONNECTIONS)
    print(f"Server started at {SERVER_IP}:{SERVER_PORT}")

    while True:
        conn_sock, addr = s.accept()
        print(f"Client: {addr} connected!")
        with conn_sock as cs:

            data = conn_sock.recv(CLIENT_CONN_BUF_SIZE)
            if not data: break
            print(repr(data))


