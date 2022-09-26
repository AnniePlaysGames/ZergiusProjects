import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8888))

sending_message = input("Сообщение: ")
sock.send(sending_message.encode())

message = sock.recv(1024)
print(message.decode("utf-8"))
sock.close()
