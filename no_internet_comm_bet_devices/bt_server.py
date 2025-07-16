# Overview: Bluetooth enables short-range communication between devices.
# Implementation Steps:
    # Use a library like pybluez (for Python) or native Bluetooth APIs (Android, iOS, etc.).
    # One device acts as a Bluetooth server, and the other acts as a client.
    # Establish a connection and exchange messages.

# pip install pybluez

import bluetooth
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# The correct format for Bluetooth MAC addresses uses colons (:), not dashes (-).
server_sock.bind(("50:5A:65:B8:E8:E8", bluetooth.PORT_ANY))
server_sock.listen(1)
port = server_sock.getsockname()[1]
print(f"Waiting for connection on port {port}")
client_sock, client_info = server_sock.accept()
print(f"Accepted connection from {client_info}")
data = client_sock.recv(1024)
print(f"Received: {data.decode()}")
client_sock.send("Hello from server".encode())
client_sock.close()
server_sock.close()

# Verify the Server Address and Port

    # Server Address: Ensure that the server_address in your client code matches the Bluetooth MAC address of the server device. On Windows, you can find the MAC address in the Bluetooth settings or through the command: ipconfig /all

    # Look for your Bluetooth adapter under "Wireless LAN Adapter" or "Bluetooth Network Connection". The MAC address will be listed as the Physical Address (e.g., 00:1A:7D:DA:71:13).

    # Option 1: Use PORT_ANY
    # If you use bluetooth.PORT_ANY in the server code, the system will assign an available port automatically.
    # You can retrieve the assigned port using:

        # port = server_sock.getsockname()[1]
        # print(f"Assigned port: {port}")

    # Option 2: Use a Fixed Port
        # Common ports for Bluetooth communication range from 1 to 30.
        # Select a specific port manually (e.g., 1, 3, or 5).

# Look for the "Physical Address" under the Bluetooth adapter.

    # Port: Use the same port number in both the server and client scripts. Bluetooth RFCOMM communication typically uses ports 1–30. Ensure the server is listening on the specified port.

# Test the Connection with a Discovery Script
# To ensure the devices are discoverable and can communicate:
# Use this discovery script to check if the server is detectable:

    # import bluetooth

    # print("Searching for devices...")
    # devices = bluetooth.discover_devices(lookup_names=True)

    # for addr, name in devices:
    #     print(f"Found device: {name} ({addr})")
    # If the server is not listed, verify that Bluetooth is enabled and the server is in discoverable mode.

# Bluetooth MAC Address Format:

    # The MAC address should be formatted with colons (:), e.g., XX:XX:XX:XX:XX:XX.
    # Using dashes (-) will result in the OSError: An invalid argument was supplied.

# Using bind:

    # bind associates the Bluetooth socket with a specific adapter and port.
    # If you're unsure about the exact MAC address of the adapter, you can use "" as the address to bind to any available Bluetooth adapter


# Run the following Python script to list available Bluetooth adapters and confirm your setup:

    # import bluetooth

    # print("Local Bluetooth adapter MAC address:")
    # local_adapter = bluetooth.read_local_bdaddr()
    # print(local_adapter[0])  # Prints the first Bluetooth adapter's MAC address

    # print("\nTesting Bluetooth socket:")
    # server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    # server_sock.bind(("", bluetooth.PORT_ANY))
    # port = server_sock.getsockname()[1]
    # print(f"Socket bound to port {port}")
    # server_sock.close()





