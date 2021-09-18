import os
import socket

S_FILE = 'test.socket'

print("Подключение")
if os.path.exists(S_FILE):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect(S_FILE)
    print("Подключено")
    print("Отправьте 'STOP' для завершения")
    while True:
        try:
            data = input("> ")
            if data != "":
                print(f"ОТПРАВЛЕНО: {data}")
                client.send(data.encode('utf-8'))
                if data == "STOP":
                    print("Отключение")
                    break
        except KeyboardInterrupt:
            print("Отключение")
            break
    client.close()
else:
    print("Ошибка подключения")
print("Отключено")
