from socket import *
import threading


def send(_socket):
    while True:
        message = input()

        if message == '/exit':
            break

        _socket.send(message.encode('utf-8'))

    _socket.close()


def receive(_socket):
    while True:
        print((_socket.recv(1024)).decode('utf-8'))


tcp_socket = socket(AF_INET, SOCK_STREAM)
host = '169.254.33.10'
port = 12229

tcp_socket.connect((host, port))
print('Connected to %s\'s chat room.' % host)
print((tcp_socket.recv(1024)).decode('utf-8'))

sender = threading.Thread(target=send, args=(tcp_socket, ))
receiver = threading.Thread(target=receive, args=(tcp_socket, ))
receiver.daemon = True

sender.start()
receiver.start()
