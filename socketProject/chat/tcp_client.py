import threading
import time
import socket
import json

SERVER_ADDRESS = ("192.168.0.11", 8000)


class ChatClient:
    _sock: socket

    def connect_to_server(self, server_address: tuple):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self._sock:
            self._sock.connect(server_address)
            threading.Thread(target=self._start_receive_loop).start()
            threading.Thread(target=self._start_input_loop).start()

    def disconnect(self):
        if not self._sock is None:
            self._sock.close()

    def _start_receive_loop(self):
        timeout_in_seconds = 10
        timeout_start = time.time()

        while True:
            if time.time() < timeout_start + timeout_in_seconds:
                continue
            else:
                timeout_start = time.time()
                response = self._sock.recv(2048)
                print(response)

    def _start_input_loop(self):
        while True:
            json_data = json.dumps((self._sock.getsockname(), input("Введите сообщение: ")))
            self._sock.send(json_data.encode())


if __name__ == '__main__':
    new_client = ChatClient()
    new_client.connect_to_server(SERVER_ADDRESS)
