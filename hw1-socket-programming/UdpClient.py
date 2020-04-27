from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
host = '169.254.33.10'
port = 12227

while True:
    data = input(">>> ")

    if data == "/exit":
        break

    udp_socket.sendto(data.encode('utf-8'), (host, port))

udp_socket.close()
