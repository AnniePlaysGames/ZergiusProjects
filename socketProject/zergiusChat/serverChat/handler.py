import socketserver


class Handler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        msg = self.request.recv(1024).strip()
        if msg.decode("utf-8") != "":
            self.request.sendall(msg)
