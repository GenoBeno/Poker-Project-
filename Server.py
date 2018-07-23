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
connPlayers = {}
playersCards = {}
flop = []
turn = ""
river = ""
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
            # connPlayers[connectors[x]] = x+1
            connPlayers.update({connectors[x] : x+1})
            print(connPlayers[connectors[x]])
        break

def giveHands():
    for x in connectors:
        card1 = deck.getTopCard()
        card2 = deck.getTopCard()
        playersCards.update({connPlayers[x] : [card1, card2]})
        print(playersCards[connPlayers[x]])
        serList = pickle.dumps(playersCards[connPlayers[x]])
        while True:
            x.sendall(serList)
        s.close()

# def askDecisions():
#     for x in connectors:

def showFlop():
    for x in range(3):
        flop.append(deck.getTopCard())

    while True:
        for x in connectors:
            serList = pickle.dumps(flop)
            x.sendall(serList)
            break
                
def newRound():
    global deck
    deck = Deck()
    giveHands()
    # askDecisions
    showFlop()

newRound()
        



