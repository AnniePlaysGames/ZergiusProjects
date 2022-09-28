import socketserver


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        data = self.request.recv(1024).strip()
        print(f"Address: {self.client_address}")
        print(f"Data: {data.decode()}")
        if data == "fuck you".encode():
            self.request.sendall("сам пошёл, мразь".encode())


if __name__ == '__main__':
    with ThreadingTCPServer(("192.168.0.11", 5000), TCPHandler) as server:
        server.serve_forever()
