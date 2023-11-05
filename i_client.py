""" Use AF_INET (client)"""
import socket

from settings import BUFFER_SIZE, TCP_IP, TCP_PORT

socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_.connect((TCP_IP, TCP_PORT))
socket_.send(b"message data in bytes")
data = socket_.recv(BUFFER_SIZE)
socket_.close()

print(f"::: received data: {data}")
