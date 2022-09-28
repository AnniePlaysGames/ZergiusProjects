from socket import socket


def send_msg_to_server(client: socket, run):
    while run:
        msg = input("enter msg")
        client.send(msg.encode())
