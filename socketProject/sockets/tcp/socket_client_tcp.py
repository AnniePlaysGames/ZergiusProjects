import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.0.11", 5000))

sending_message = input("Сообщение: ")
sock.send(sending_message.encode())

message = sock.recv(1024)
print(message.decode("utf-8"))
sock.close()
