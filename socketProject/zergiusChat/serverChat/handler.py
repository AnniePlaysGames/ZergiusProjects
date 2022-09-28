import socketserver


class Handler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        msg = self.request.recv(1024).strip()
        self.request.sendall(msg)
