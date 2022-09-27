import socketserver


class Handler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        msg, adres = self.request.recv(1024).strip()
        print(f"{msg} from {adres}")
