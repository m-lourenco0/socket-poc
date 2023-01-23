from socket import socket, AF_INET, SOCK_DGRAM
from dynaconf import settings

s = socket(AF_INET, SOCK_DGRAM) #create UDP socket
s.bind(('', settings.PORT))

while 1:
    data, addr = s.recvfrom(1024) #wait for a packet
    data = data.decode()
    if data.startswith(settings.MAGIC):
        print("got service announcement from", data[len(settings.MAGIC):])
        break