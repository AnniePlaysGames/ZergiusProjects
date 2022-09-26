import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
sock.setblocking(True)

while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    except socket.error:
        print("no clients")
    else:
        client.setblocking(True)
        result = client.recv(1024)
        client.close()
        print("Message", result.decode("utf-8"))
        print(f"port is {addr}")
