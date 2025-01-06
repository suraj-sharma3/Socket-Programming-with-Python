import bluetooth
server_address = "XX:XX:XX:XX:XX:XX"  # Replace with server's Bluetooth address
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((server_address, port))
sock.send("Hello from client".encode())
data = sock.recv(1024)
print(f"Received: {data}")
sock.close()