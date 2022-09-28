import socket
import threading

from zergiusChat.constants import *
from zergiusChat.clientChat.listen_server import listen_server
from zergiusChat.clientChat.send_msg_to_server import send_msg_to_server


def main():
    run = True
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))

    thread_listen = threading.Thread(target=listen_server, args=(client, run))
    thread_send = threading.Thread(target=send_msg_to_server, args=(client, run))

    thread_listen.start()
    thread_send.start()



if __name__ == '__main__':
    main()
