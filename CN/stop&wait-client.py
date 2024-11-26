import socket, time 

HOST = '127.0.0.1'
PORT = 5001
TIMEOUT = 5

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    data = input("Enter msg: ")
    client.sendall(data.encode())
    if data == 'end':
        break
    client.settimeout(TIMEOUT)
    try:
        msg = client.recv(1024)
        print(msg.decode())
    except socket.timeout:
        print("Timeout exceeded, retransimitting data...")
        client.sendall(data.encode())
client.close()
