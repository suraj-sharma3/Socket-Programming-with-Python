# a server can process requests from multiple clients which are connected to it
# The server can communicate with all its clients i.e, all the devices whether they are computers, smartphones, IoT devices, gaming devices, home appliances, etc
# The client and server communicate with each other using IP addresses and port numbers
# The client communicates with the server at an IP address with a port number
# If the client is trying to communicate with the server using its IP address at port 9090, that port of the server should be available for communication, only then communication can happen
# Example : Consider a house (server) which has an address (IP address) and lets say the house has several doors (ports) through which a person can enter the house. Now if a person (client) has to go inside the house, the person should have the house's address (IP address) and the number of the door which is open, lets say door 3 (port number), If the person (client) tries to enter the house (server) from door 3 (port open for communication), only then the communication can happen.
# Command to check local IP address : windows - ipconfig | mac and linux - ifconfig
# Communication between devices with the local IP address can only happen if they are on the same local area network
# For communication between devices on the internet can only happen with the public IP address
# Local IP address could be same for a lot of devices but the public IP address wouldn't be the same for any pair of devices
# A Socket is just a communication end point, if 2 devices want to communicate with each other, the 2 devices can be considered as 2 sockets
# A socket could be an internet socket, bluetooth socket, OS socket, infrared socket etc. for e.g. AF_INET is internet socket, AF_BLUETOOTH is bluetooth socket

# AF_INET -> IPV4 and AF_INET6 -> IPV4

# once we have selected whether our socket is an internet socket or some other type of socket we have to choose whether it is a SOCK_STREAM (follows TCP) or SOCK_DGRAM (follows UDP)

# SOCK_STREAM socket is a connection based socket, so the communication can only happen if the connection is there, once the connection terminates, the connection stops
# In SOCK_DGRAM (user datagram socket), individual messages are exchanged between the sockets, there is no connection, its just the 1 socket sends the message to the other socket 

# TCP is more reliable than UDP as it can detect data packet loss because it is connection based, In TCP if a data packet is sent and it is received then we get a message that it is received

# In UDP if a data packet is lost during transmission, it is lost

# In TCP the messages are received in the order in which they were sent
# In UDP the messages are not received in the order in which they were sent

# TCP is a bytestream and it keeps up the connection

# In UDP one datagram is sent at a time and the datagrams could be received in a different order
# UDP is comparatively more real time
# UDP is faster and creates less network and PC stress

# TCP is used when data loss during transmission has to be avoided like sending images, data, etc
# UDP is used when some data loss is not a problem, nott every bit of data is important. e.g. video conferencing