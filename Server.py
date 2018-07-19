import pygame
import time
import socket
# import Player from Player

pygame.init()

s = socket.socket()
port = 20000
host = socket.gethostbyname(socket.gethostname())
s.bind((host,port))
s.listen(5)
connectors = []
players = []

# def giveHands():
#     for x in connectors:


s.settimeout(10)
while True:
    try:
        c, addr = s.accept()
        print('got cnection from', addr)

        # c.send('Tank you for connecting with your friendly neighborhood spiderman'.encode())
        # message = (c.recv(1024))
        # print (message)
        connectors.append(c)
    except socket.timeout as e:
        numPlayers = len(connectors)
        for x in range (numPlayers):
            connectors[x].send((str(numPlayers) + str(x+1)).encode())
        break


    # connectors[x].send(str(int(x+1)).encode())
        



