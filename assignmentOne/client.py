import socket

# Define server information
server_ip = "50.123.106.98"  
server_port = 5001       

# Get user input
client_name = input("Enter your name: ")
client_number = input("Enter an integer between 1 and 100: ")

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

# Prepare data to send
data = "{},{}".format(client_name, client_number)

# Send data to the server
client_socket.send(data.encode())

# Receive and print the server's response
server_response = client_socket.recv(1024).decode()
print("Server response: {}".format(server_response))

# Close the client socket
client_socket.close()
