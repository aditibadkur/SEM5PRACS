def crc(data, divisor):
    n = len(divisor)
    temp = data+'0'*(n-1)
    temp = list(temp)
    divisor = list(divisor)
    for i in range(len(data)):
        if temp[i] == "1":
            for j in range(n):
                temp[i+j] = str(int(temp[i+j]) ^ int(divisor[j]))
    remainder = "".join(temp[-n+1:])
    return remainder
    
def crc2(data, divisor):
    n = len(divisor)
    # data += (n-1)*0
    temp = list(data)
    divisor = list(divisor)
    for i in range(len(data)-n+1):
        if temp[i] == "1":
            for j in range(n):
                temp[i+j] = str(int(temp[i+j]) ^ int(divisor[j]))
    remainder = "".join(temp[-n+1:])
    return remainder

data = input("Enter data to be sent: ")
key = input("Enter key: ")

checksum = crc(data, key)
sent_data = data + checksum
print(f"Sent data: {sent_data}")

#Receiver side
received_data = input("Enter received data: ")
remainder = crc2(received_data, key)

if int(remainder) == 0:
    print("Data received without errors.")
else:
    print(f"Error detected in received data. Remainder: {remainder}")
