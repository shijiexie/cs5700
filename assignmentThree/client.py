from socket import *
import ssl
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Gmail credentials
username = "jiesj09@gmail.com"
password = "mypassword"  

# Mail server details
mailserver = "smtp.gmail.com"
mailport = 587

# Create socket and establish a TCP connection
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailport))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Start TLS
starttlsCommand = 'STARTTLS\r\n'
clientSocket.send(starttlsCommand.encode())
recv = clientSocket.recv(1024).decode()
print("STARTTLS response:", recv)
if recv[:3] != '220':
    print('220 reply not received from server after STARTTLS command.')

# Wrap the socket with SSL
clientSocket = ssl.wrap_socket(clientSocket)

# Base64 encode username and password
encodedUsername = base64.b64encode(username.encode()).decode()
encodedPassword = base64.b64encode(password.encode()).decode()

# Authenticate
authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recv = clientSocket.recv(1024).decode()
print("AUTH LOGIN response:", recv)

clientSocket.send((encodedUsername + '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print("Username response:", recv)

clientSocket.send((encodedPassword + '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print("Password response:", recv)

# Create a MIME multipart message
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = "styumi@163.com"  # Replace with recipient's email address
msg['Subject'] = "TEST OF DD"

# Attach text part
text = "I love computer networks!"
msg.attach(MIMEText(text, 'plain'))

# Attach image part
filename = "/Users/xieshijie/Desktop/cs5700/Assignment/WeChatf43302ce3dfbddd8f07f20d1d24f1380.png"  # Specify the path to your image
try:
    with open(filename, 'rb') as f:
        image = MIMEImage(f.read())
        msg.attach(image)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    exit(1)

# Convert the message to a string
formatted_msg = msg.as_string()

# Send MAIL FROM command and print server response
mailFromCommand = "MAIL FROM:<{}>\r\n".format(username)
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Send RCPT TO command and print server response
rcptToCommand = "RCPT TO:<styumi@163.com>\r\n"  # Replace with recipient's email address
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

# Send DATA command and print server response
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)

# Send message data
clientSocket.send(formatted_msg.encode())
endmsg = "\r\n.\r\n"
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024).decode()
print(recv_msg)

# Send QUIT command and get server response
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)

# Close the socket
clientSocket.close()
