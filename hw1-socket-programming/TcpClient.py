from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
host = '169.254.33.10'
port = 12227

tcp_socket.connect((host, port))

print('Connected to %s\'s chat room.' % host)
print((tcp_socket.recv(1024)).decode('utf-8'))

while True:
    message = input(">>> ")

    tcp_socket.send(message.encode('utf-8'))

    if message == '/exit':
        break

    print('[Waiting response...]')
    print('admin : %s' % (tcp_socket.recv(1024)).decode('utf-8'))

tcp_socket.close()
