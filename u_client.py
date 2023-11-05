""" Use AF_UNIX and socket file (client)"""
import os
import socket

from settings import SOCKET_FILE

print("::: Connecting...")
if os.path.exists(SOCKET_FILE):
    client = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_DGRAM)
    client.connect(SOCKET_FILE)
    print("::: Connected")
    print("::: Send 'stop' for closing connection")
    while True:
        try:
            data = input("> ")
            if data != "":
                print(f"::: Sent: {data}")
                client.send(data.encode("utf-8"))
                if data.lower() == "stop":
                    print("::: Disconnecting...")
                    break
        except KeyboardInterrupt:
            print("::: Disconnecting...")
            break
    client.close()
else:
    print("::: Connection error")
print("::: Diconnected")
