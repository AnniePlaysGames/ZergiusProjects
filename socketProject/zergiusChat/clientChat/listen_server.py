from socket import socket, error
from time import  sleep


def listen_server(client: socket, run):
    while run:
        msg = client.recv(1024)
        if msg.decode("utf-8") != "":
            print(msg.decode("utf-8"))
        sleep(1 / 60)
