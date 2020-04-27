from socket import *
import threading


def create_link(_socket):
    global user_no

    thread.append(Communication(_socket))

    thread[user_no].daemon = True

    thread[user_no].start()


class Communication(threading.Thread):
    def __init__(self, _socket):
        super().__init__()
        self.message = None
        self.user_id = None
        self.tcp_socket = _socket
        self.name = str([])

    def run(self):
        global user_no

        self.message, self.user_id = self.tcp_socket.accept()
        notification_welcome = 'Welcome to our chat room. Say Hi!'

        self.message.send(notification_welcome.encode('utf-8'))

        notification_entrance = ('%s has connected.' % (self.user_id[1]))

        print(notification_entrance)
        self.notify(notification_entrance)

        self.name = str(user_no)
        user_no += 1

        create_link(self.tcp_socket)

        _thread = threading.Thread(target=self.receive)
        _thread.daemon = True

        _thread.start()

    def receive(self):
        while True:
            data = (self.message.recv(4096)).decode('utf-8')

            if data == '/exit':
                relay = ('%s has left chat room.' % (self.user_id[1])).encode('utf-8')

                print(relay.decode('utf-8'))
                self.exit()
                self.send_to_client(relay)

                break
            else:
                relay = ('%s : %s' % (self.user_id[1], data)).encode('utf-8')

                print(relay.decode('utf-8'))
                self.send_to_client(relay)

    def exit(self):
        global user_no

        check = '(' + self.name

        for i in range(0, user_no):
            if check in str(thread[i]):
                del thread[i]

                user_no -= 1

                break

        self.message.close()

    @staticmethod
    def send_to_client(_message):
        try:
            for user in thread:
                user.message.send(_message)
        except Exception as _exception:
            pass

    @staticmethod
    def notify(_notification):
        notifier = ('**** %s ****' % _notification)
        for _users in thread:
            _users.message.send(notifier.encode('utf-8'))


thread = []
user_no = 0

tcp_socket = socket(AF_INET, SOCK_STREAM)
host = gethostname()
port = 12229

tcp_socket.bind((host, port))
tcp_socket.listen()

create_link(tcp_socket)

while True:
    notification = input()

    try:
        for users in thread:
            users.notify(notification)
    except Exception as exception:
        pass
