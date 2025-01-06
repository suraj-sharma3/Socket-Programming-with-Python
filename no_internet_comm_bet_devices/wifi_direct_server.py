# To implement client-server communication between two devices without an internet connection, you can use local communication methods such as:

# 1. Wi-Fi Direct
    # Overview: Wi-Fi Direct allows devices to establish a direct peer-to-peer connection without requiring a router or internet.
    # Implementation Steps:
        # Server (Device 1):
            # Create a Wi-Fi Direct group.
            # Host a socket server on a specified port.
        # Client (Device 2):
            # Join the Wi-Fi Direct group.
            # Connect to the server's IP address and port.
        # Code Example:
            # Use libraries like Python's socket module for communication.

# Server
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.0.100', 12345))  # Bind to any local IP
server_socket.listen(1)
print("Waiting for a connection...")
conn, addr = server_socket.accept()
print(f"Connected to {addr}")
data = conn.recv(1024).decode()
print(f"Received: {data}")
conn.sendall("Message received".encode())
conn.close()


