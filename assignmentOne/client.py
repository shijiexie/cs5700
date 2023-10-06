import socket

server_ip = "10.18.40.117"  
server_port = 6767       

client_name = input("Enter your name: ")
client_number = input("Enter an integer between 1 and 100: ")

# Create a socket for the client and connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
data = "{},{}".format(client_name, client_number)

# Send data to the server
client_socket.send(data.encode())
server_response = client_socket.recv(1024).decode()

# Receive and print the server's response
try:
    # Receive and print the server's response
    server_name, server_number = server_response.split(',')
    server_number = int(server_number)

    client_number = int(client_number)
    total_sum = client_number + server_number

    print("Client Name: {}".format(client_name))
    print("Server Name: {}".format(server_name))
    print("Client Number: {}".format(client_number))
    print("Server Number: {}".format(server_number))
    print("Sum: {}".format(total_sum))
    client_socket.close()

except Exception as e:
    print("Error: You should enter a number in range 0 to 100")
    client_socket.close()




