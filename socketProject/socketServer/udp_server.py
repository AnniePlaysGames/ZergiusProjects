import socketserver


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        data, socket = self.request
        print(f"Address: {self.client_address}")
        print(f"Data: {data.decode()}")
        socket.sendto(data, self.client_address)


if __name__ == '__main__':
    with socketserver.UDPServer(("0", 8888), UDPHandler) as server:
        server.serve_forever()
