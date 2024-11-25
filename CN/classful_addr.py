ip_addr = input("Enter ip address: ")
ip = ip_addr.split(".")
firstoctet = int(ip[0])
secondoctet = int(ip[1])
thirdoctet = int(ip[2])
fourthoctet = int(ip[3])

# print(firstoctet, secondoctet, thirdoctet, fourthoctet)
if (0 < firstoctet < 128):
    print("A")
    print("Subnet Mask: 255.0.0.0")
    print(f"First address: {firstoctet}.0.0.0")
    print(f"Last address: {firstoctet}.255.255.255")
    
elif (127 < firstoctet < 192):
    print("B")
    print("Subnet Mask: 255.255.0.0")
    print(f"First address: {firstoctet}.{secondoctet}.0.0")
    print(f"Last address: {firstoctet}.{secondoctet}.255.255")
    
elif (191 < firstoctet < 224):
    print("C")
    print("Subnet Mask: 255.255.255.0")
    print(f"First address: {firstoctet}.{secondoctet}.{thirdoctet}.0")
    print(f"Last address: {firstoctet}.{secondoctet}.{thirdoctet}.255")
    
elif (223 < firstoctet < 240):
    print("D")
    print("Multicast")
    
elif (239 < firstoctet < 255):
    print("E")
    print("Reserved")
    
else:
    print("INVALID IP ADDRESS")
