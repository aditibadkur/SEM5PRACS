import socket, time

bucket = 10
current = 0

def leak_rate():
    global current
    leak = 2
    if current>0:
        current-= leak
        print(f"Leaked: {leak}, Current: {current}")
    else:
        print("Bucket empty")

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 12345))

while True:
    data, addr = server.recvfrom(1024)
    packet_size = int(data.decode())
    
    if current+packet_size<=bucket:
        current += packet_size
        print(f"Packets of size {packet_size} recvd")
    else:
        print("Bucket full, no more data is allowed")
    
    leak_rate()
    time.sleep(1)
