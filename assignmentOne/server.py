import socket
import threading

server_ip = "10.18.40.117"
server_port = 6767

# Function to handle client requests
def handle_client(client_socket):
    try:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        client_name, client_number = data.split(',')

        server_number = 33
        server_response = "Server of Shijie,{}".format(server_number)

        if 1 <= int(client_number) <= 100:
            client_number = int(client_number)
            sum_values = client_number + server_number
            client_socket.send(server_response.encode())

            print("Client Name: {}".format(client_name))
            print("Server Name: Server of Shijie")
            print("Client Number: {}".format(client_number))
            print("Server Number: {}".format(server_number))
            print("Sum: {}".format(sum_values))
        else:
            client_socket.send("Error: Integer out of range (1-100)".encode())
    except Exception as e:
        print("Error handling client:", e)
    finally:
        # Close the client socket
        client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_ip, server_port))

server_socket.listen(5)  # Allow up to 5 connections at a time

print("Server is listening on {}:{}".format(server_ip, server_port))

while True:
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from {}:{}".format(client_address[0], client_address[1]))

    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
