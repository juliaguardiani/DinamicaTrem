import socket
import sys

serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
print("Do Ctrl+c to exit the program !!")

# Let's send data through UDP protocol
while True:
    send_data = input("Envie a letra que representa a alteracao da velocidade desejada=>");
    s.sendto(send_data.encode('utf-8'), (serverAddressPort))
    print("\n 1. Client Sent : ", send_data, "\n")
    data, address = s.recvfrom(bufferSize)
    print("\n2. Client received : ", data.decode('utf-8'), "\n")
# close the socket
s.close()