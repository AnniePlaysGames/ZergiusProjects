import threading
import socket
import json

SERVER_ADDRESS = ("127.0.0.1", 8000)


class ChatClient:
    _sock: socket

    def connect_to_server(self, server_address: tuple):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect(server_address)

        threading.Thread(target=self._start_receive_loop).start()
        threading.Thread(target=self._start_input_loop).start()

    def _start_receive_loop(self):
        while True:
            response = self._sock.recv(2048)
            json_data = json.loads(response)
            print(f"{json_data[0]} {json_data[1]}")

    def _start_input_loop(self):
        while True:
            json_data = json.dumps((self._sock.getsockname(), input()))
            if json_data != "":
                self._sock.send(json_data.encode())


if __name__ == '__main__':
    new_client = ChatClient()
    new_client.connect_to_server(SERVER_ADDRESS)
