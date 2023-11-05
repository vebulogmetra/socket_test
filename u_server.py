""" Use AF_UNIX and socket file (server)"""
import os
import socket

from settings import SOCKET_FILE

if os.path.exists(SOCKET_FILE):
    os.remove(SOCKET_FILE)

print("::: Open socket")
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind(SOCKET_FILE)

while True:
    data = server.recv(2048)
    if not data:
        break
    else:
        print("<" * 25)
    print(data)
    if str(data).lower() == "stop":
        break
print("::: Close socket")
server.close()
os.remove(SOCKET_FILE)
