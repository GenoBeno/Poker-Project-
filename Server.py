import pygame
from time import * 
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
        # while True:
        x.send(serList)
        sleep(3)

# def askDecisions():
#     for x in connectors:

def showFlop():
    for x in range(3):
        flop.append(deck.getTopCard())
    print("Flop: " + str(flop))

    for n in connectors:
        serList = pickle.dumps(flop)
        print("sending flop")
        n.sendall(serList)

    sleep(3)

def showTurn():
    for x in connectors:
        serCard = pickle.dumps(deck.getTopCard())
        x.sendall(serCard)
        sleep(1)

def showRiver():
    for x in connectors:
        serCard = pickle.dumps(deck.getTopCard())
        x.sendall(serCard)
            
                
def newRound():
    global deck
    deck = Deck()
    giveHands()
    # askDecisions
    showFlop()
    showTurn()
    showRiver()

newRound()
        



