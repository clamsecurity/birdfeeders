import socket

target_host = "127.0.0.1"
target_port = 9997

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data
client.sendto(b"ALPHA-BRAVO-CHARLIE", (target_host, target_port))

# Receive data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()