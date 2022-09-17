import socket

target_host = "www.google.com"
target_port = 80

# Create a socket object
# AF_INET means using the standard IPv4 address or hostname
# SOCK_STREAM means this will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((target_host, target_port))

# Send data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive data
response = client.recv(4096)

print(response.decode())
client.close()