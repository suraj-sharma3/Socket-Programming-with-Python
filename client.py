# go to myip.is website to check your system's public IP address

import socket
host = "192.168.0.197" # if the client and server are in a local area network then we can enter the private IP address of the server # We have to provide the server's IP address and not the client's IP address
port = 9090 # port on which the server is listening

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # the socket here is a connection endpoint

socket.connect((host, port)) # To connect to the server

socket.send("Hello Server!".encode('utf-8')) # to send a message to the server

print(socket.recv(1024).decode('utf-8')) # to receive message from the server
