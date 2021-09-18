import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 8001
BUFFER_SIZE = 1024
MESSAGE = b'message data bytes'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print(f"received data: {data}")
