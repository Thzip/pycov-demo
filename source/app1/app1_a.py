import socket


class App1A(object):
    def __init__(self):
        pass

    def app1_a_m1_get_ip(self):
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip

    def app1_a_m2(self):
        pass
