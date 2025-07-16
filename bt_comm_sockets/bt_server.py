# Like client server communication implemented previously, here also there will be a socket but this time, the socket will be bound to a MAC / Physical / Hardware address
# The server will listen for incoming connection, it will accept incoming connections and handle them

import socket

bt_server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
# socket.BTPROTO_RFCOMM - protocol for bluetooth communication

# In the OS model, IP layer is above the MAC / Hardware address

# for bluetooth MAC address, go to device manager -> bluetooth -> find your bluetooth adapter (e.g. Realtek bluetooth 5 adapter) -> open properties -> go to advanced -> the MAC address (hexadecimal values separated by colons) is specified in the address field

# OR

# run ipconfig /all command in cmd and take the physical address from the bluetooth adapter section 

# to bind the "bt_server" socket to the MAC address, we can use the bind function and provide it the MAC address as well as the channel number and not the port number

# RFCOMM (Serial Port Emulation):
    # RFCOMM supports 30 channels, numbered 1 to 30.
    # These are analogous to TCP/UDP ports in internet-based socket programming.
    # Usage of Channels:
    # Port 1 is typically used for standard services like the Bluetooth Serial Port Profile (SPP).
    # Other ports are available for custom applications.

bt_server.bind(("50:5A:65:B8:E8:E8", 4)) # MAC address and BT channel 

bt_server.listen(1) # Listen for 1 connection

client, addr = bt_server.accept() # client over here is the object that helps the server script communicate with the client script running on the other device

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message : {data.decode('utf-8')}")
        message = input("Enter Message : ")
        client.send(message.encode('utf-8'))
except OSError as e:
    pass

client.close()
bt_server.close()