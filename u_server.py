import os
import socket

S_FILE = 'test.socket'

if os.path.exists(S_FILE):
    os.remove(S_FILE)

print("Открываем сокет")
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind(S_FILE)

while True:
    data = server.recv(2048)
    if not data:
        break
    else:
        print('='*25)
    print(data)
    if data == b'STOP':
        break
print('='*25)
print("Закрываем сокет")
server.close()
os.remove(S_FILE)
