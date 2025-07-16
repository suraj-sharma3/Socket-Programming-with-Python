import bluetooth

server_address = "50:5A:65:B8:E8:E8"  # Replace with the correct server's Bluetooth address
port = 4  # Match this with the server's port

try:
    # Create a Bluetooth socket
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    
    # Connect to the server
    print(f"Connecting to {server_address} on port {port}...")
    sock.connect((server_address, port))
    print("Connected successfully!")
    
    # Send and receive data
    sock.send("Hello from client".encode())
    data = sock.recv(1024)
    print(f"Received: {data.decode()}")
    
except bluetooth.BluetoothError as e:
    print(f"Bluetooth error: {e}")
except OSError as e:
    print(f"OS error: {e}")
finally:
    sock.close()
    print("Connection closed.")


