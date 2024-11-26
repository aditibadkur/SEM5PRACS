import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5001))

while True:
    data = input("Enter data: ")
    if data == 'end':
        break
    client.sendto(data.encode())
client.close()
    
