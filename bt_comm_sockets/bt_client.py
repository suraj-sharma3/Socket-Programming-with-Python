import socket

bt_client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

bt_client.connect(("50:5A:65:B8:E8:E8", 4))

try:
    while True:
        message = input("Enter Message : ")
        bt_client.send(message.encode('utf-8'))

        data = bt_client.recv(1024)
        if not data:
            break
        print(f"Message : {data.decode('utf-8')}")
except OSError as e:
    pass

bt_client.close()

# Put the bt_client script on the client machine and the bt_server script on the server machine
# Turn on the bluetooth on both client and server machines and make sure the device is discoverable
# Run both the scripts on both the machines and then server and client can communicate with each other
