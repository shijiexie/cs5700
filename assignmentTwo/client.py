import socket
import time

server_address = ('localhost', 12000)  

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)

num_pings = 10

# Initialize variables for tracking RTT, minimum RTT, maximum RTT, and lost packets
rtt_list = []
min_rtt = float('inf')
max_rtt = 0
lost_packets = 0

for sequence_number in range(1, num_pings + 1):
    send_time = time.time()

    message = f'Ping {sequence_number} {send_time}'.encode()

    try:
        client_socket.sendto(message, server_address)
        response, server_address = client_socket.recvfrom(1024)

        # Calculate the round-trip time (RTT)
        receive_time = time.time()
        rtt = receive_time - send_time

        rtt_list.append(rtt)
        min_rtt = min(min_rtt, rtt)
        max_rtt = max(max_rtt, rtt)

        print(f'Response from {server_address}: {response.decode()} | RTT: {rtt:.6f} seconds')

    except socket.timeout:
        lost_packets += 1
        print(f'Ping {sequence_number} Request timed out')

packet_loss_rate = (lost_packets / num_pings) * 100

print("\nPing statistics:")
print(f"Minimum RTT: {min_rtt:.6f} seconds")
print(f"Maximum RTT: {max_rtt:.6f} seconds")
print(f"Average RTT: {sum(rtt_list) / num_pings:.6f} seconds")
print(f"Packet Loss Rate: {packet_loss_rate:.2f}%")

# Close the socket
client_socket.close()
