# Client
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.0.100', 12345))  # Replace with server IP
client_socket.sendall("Hello Server".encode())
data = client_socket.recv(1024).decode()
print(f"Received: {data}")
client_socket.close()