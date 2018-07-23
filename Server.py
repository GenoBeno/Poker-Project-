import pygame
import time
import socket, pickle
from Deck import Deck
from Card import Card
# import Player from Player

pygame.init()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 20000
host = socket.gethostbyname(socket.gethostname())
s.bind((host,port))
s.listen(5)
connectors = []
# global deck
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

def giveHands():
    # connectors[0].send(str(deck.getTopCard()).encode())
    for x in connectors:
        serializedCard1 = pickle.dumps(deck.getTopCard())
        serializedCard2 = pickle.dumps(deck.getTopCard())
        x.send(serializedCard1)
        s.settimeout(5)
        while True:     
            try: 
                x.send(serializedCard2)
            except socket.timeout as e:
                break
                
def newRound():
    global deck
    deck = Deck()
    giveHands()

newRound()
        



