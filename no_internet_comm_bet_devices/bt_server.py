# Overview: Bluetooth enables short-range communication between devices.
# Implementation Steps:
    # Use a library like pybluez (for Python) or native Bluetooth APIs (Android, iOS, etc.).
    # One device acts as a Bluetooth server, and the other acts as a client.
    # Establish a connection and exchange messages.

# pip install pybluez

import bluetooth
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)
port = server_sock.getsockname()[1]
print(f"Waiting for connection on port {port}")
client_sock, client_info = server_sock.accept()
print(f"Accepted connection from {client_info}")
data = client_sock.recv(1024)
print(f"Received: {data}")
client_sock.send("Hello from server".encode())
client_sock.close()
server_sock.close()


