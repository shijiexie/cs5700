from socket import *
import random

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', 12000))

while True:
    rand = random.randint(0, 10)
    received_message, address = serverSocket.recvfrom(1024)
    received_message = received_message.decode()
    
    # Print the received message as the rubrics required
    print(f"Received from {address}: {received_message}")
    
    received_message = received_message.encode().upper()

    if rand < 4:
        continue

    # Send the message back to the client
    serverSocket.sendto(received_message, address)
