from socket import *
import threading


def send(_socket):
    while True:
        _message = input()
        _socket.send(_message.encode('utf-8'))


def receive(_socket):
    while True:
        _data = (_socket.recv(1024)).decode('utf-8')

        print(user_id[1], ':', _data)

        if _data == '/exit':
            print(user_id[1], 'has left chat room.')

            break

    _socket.close()


tcp_socket = socket(AF_INET, SOCK_STREAM)
host = gethostname()
port = 12225

tcp_socket.bind((host, port))
tcp_socket.listen()

message, user_id = tcp_socket.accept()

print(str(user_id), 'has connected.')

notification_welcome = 'Welcome to our chat room. Say Hi!'

message.send(notification_welcome.encode('utf-8'))

sender = threading.Thread(target=send, args=(message, ))
sender.daemon = True
receiver = threading.Thread(target=receive, args=(message, ))

sender.start()
receiver.start()
