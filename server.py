import socket
import threading

# Define server information
server_ip = "192.168.68.52"
server_port = 5001

# Function to handle client requests
def handle_client(client_socket):
    try:
        # Receive data from the client
        data = client_socket.recv(1024).decode()

        # Extract client's name and number
        client_name, client_number = data.split(',')

        # Process the data and send a response
        server_number = 33
        server_response = "Server of Shijie,{}".format(server_number)

        if 1 <= int(client_number) <= 100:
            # Calculate the sum
            client_number = int(client_number)
            sum_values = client_number + server_number

            # Send the response back to the client
            client_socket.send(server_response.encode())

            print("Client Name: {}".format(client_name))
            print("Server Name: Server of Shijie")
            print("Client Number: {}".format(client_number))
            print("Server Number: {}".format(server_number))
            print("Sum: {}".format(sum_values))
        else:
            # Handle out-of-range input
            client_socket.send("Error: Integer out of range (1-100)".encode())
    except Exception as e:
        print("Error handling client:", e)
    finally:
        # Close the client socket
        client_socket.close()

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(5)  # Allow up to 5 connections at a time

print("Server is listening on {}:{}".format(server_ip, server_port))

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from {}:{}".format(client_address[0], client_address[1]))

    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
