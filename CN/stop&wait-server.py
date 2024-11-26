import socket, random

HOST = '127.0.0.1'
PORT = 5001
TIMEOUT = 5

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

conn, addr = server.accept(1024)

def ack(conn):
    while True:
        data = conn.recv(1024)
        msg = data.decode()
        if not data:
            break
        if msg == 'end':
            break
        # else print data
        if random.random()<0.3:
            print("simulating loss for packet")
            continue
        ack = print(f"sending frame {msg}")
        conn.sendall(ack.encode())
    conn.close()
server.close()
