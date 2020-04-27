from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
host = gethostname()
port = 12227

tcp_socket.bind((host, port))
tcp_socket.listen()

message, user_id = tcp_socket.accept()

print(str(user_id), 'has connected.')

notice = 'Welcome to our chat room. Say Hi!'

message.send(notice.encode('utf-8'))

while True:
    print('[Waiting response...]')

    data = (message.recv(1024)).decode('utf-8')

    print(user_id[1], ':', data)

    message.send((input(">>> ")).encode('utf-8'))

    if data == '/exit':
        print(user_id[1], 'has left chat room.')

        break
