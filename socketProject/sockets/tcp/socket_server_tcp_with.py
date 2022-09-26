import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(("127.0.0.1", 8888))
    sock.listen(5)
    sock.settimeout(20)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while True:
        client, adres = sock.accept()
        result = client.recv(1024)
        print(client.fileno())
        client.close()
        print(result.decode("utf-8"))