from zergiusChat.constants import IP, PORT
from handler import Handler
from server import Server


def main():
    with Server((IP, PORT), Handler) as server:
        server.serve_forever()


if __name__ == '__main__':
    main()
