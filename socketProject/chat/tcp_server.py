import json
import socketserver

SERVER_ADDRESS = ("192.168.0.11", 8000)


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        data = self.request.recv(2048)
        json_data = json.loads(data.decode("utf-8"))
        self.request.sendall(f"{json_data[0]}: {json_data[1]};".encode("utf-8"))


if __name__ == '__main__':
    with ThreadingTCPServer(SERVER_ADDRESS, TCPHandler) as server:
        server.serve_forever()
