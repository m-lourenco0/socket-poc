import socket

class Host:
    def __init__(self, ip, status):
        self.ip = ip
        self.status = status
        self.host_name = socket.gethostbyaddr(ip)[0]