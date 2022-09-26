import socket

unix_sock_name = "unix.sock"

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.sendto(b"Test message", unix_sock_name)
