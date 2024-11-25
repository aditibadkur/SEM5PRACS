import socket, time, random

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    packet_size = random.randint(1, 5)
    msg = str(packet_size)
    client.sendto(msg.encode, ('localhost', 12345))
    print(f"Sent packets of size {packet_size}")
    time.sleep(1)
