from socketserver import TCPServer, ThreadingMixIn


class Server(TCPServer, ThreadingMixIn):
    pass
