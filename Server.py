import pygame
import time
import socket
from ServerTurnActions import *

pygame.init()

s = socket.socket()
port = 20000
host = socket.gethostbyname(socket.gethostname())
s.bind((host,port))
s.listen(5)
connectors = []


print("AKJSHDFKJASHKDFJASHDJKFSJK")
s.settimeout(10)
while True:
    try:
        c, addr = s.accept()
        print('got connection from', addr)

        # c.send('Tank you for connecting with your friendly neighborhood spiderman'.encode())
        # message = (c.recv(1024))
        # print (message)
        connectors.append(c)
    except socket.timeout as e:
        break

numPlayers = len(connectors)
for x in range (numPlayers):
    connectors[x].send(str(numPlayers).encode())

#
