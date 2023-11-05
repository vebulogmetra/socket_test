""" Use AF_INET (server)"""
import socket

from settings import BUFFER_SIZE, TCP_IP, TCP_PORT

socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_.bind((TCP_IP, TCP_PORT))
socket_.listen(1)

conn, addr = socket_.accept()
print(f"::: Connection address: {addr}")
while True:
    data: bytes = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print(f"received data: {data}")
conn.close()
