from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
host = gethostname()
port = 12227

udp_socket.bind((host, port))

while True:
    data, user_id = udp_socket.recvfrom(1024)

    if data == '/exit':
        break

    print(str(user_id[1]), 'sends data.')
    print(str(user_id[1]), ':', data.decode('utf-8'))

udp_socket.close()
