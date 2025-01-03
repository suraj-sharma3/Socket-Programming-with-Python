import socket 

# ipconfig command -> either ethernet adapter address or wireless LAN -> IPv4 address -> either copy this address in host or use the below given code to get this IP address
# go to myip.is website to check your system's public IP address

host = socket.gethostbyname(socket.gethostname()) # IP address
# host = '192.168.0.197' # this is also valid
# print(host)
# if the server has to be hosted on the local system we can even do host = 'localhost' or host = '127.0.0.1'

# while choosing the port, don't choose a well known or reserved port like 80 used for HTTP or 22 which is used for SSH
# Choose the same port for client and server
port = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # This socket needs to be binded to a host to make it a server

server.bind((host, port)) # to bind the socket to the host, we pass a tuple of IP address and port number to the bind function

server.listen(10) # to listen for incoming connections on the defined port, the parameter '10' is optional and it could be any number indicating how many connections the server can accept before rejecting connection requests, so the server will only accept 10 connections and after accepting 10 connections, it will reject all other connection requests

# the server socket defined above is only for accepting connections not for communicating with the client

while True: # we will continuously look for connection requests
    communication_socket, address = server.accept() # the accept method accepts the requests and returns the socket for communication with a connection and its address # the socket here is a connection endpoint
    print(f"Connected to address {address}")
    message = communication_socket.recv(1024).decode('utf-8') # receive 1024 bytes from the client and decode it using utf-8 as the received message is encoded as a bytestream
    print(f"Message from client is {message}")
    communication_socket.send(f"Message received".encode('utf-8')) # send a message to the client after encoding it with utf-8
    communication_socket.close() # closing the communication socket, we can also keep it open if we want to
    print(f"Connection with {address} terminated")


