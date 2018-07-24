import socket
import time
import pygame
import os
from Card import Card
from Player import Player
from Poker import *
from pygame.locals import *

pygame.init()

def Check(cList, PN, screen):
    cList[PN+1].sendto('check'.encode(), cList[PN + 1])
    displayText('Checked', [(100, 100)], screen, 30)
    pygame.display.update()

def Call(cList, PN, screen):
    pass

def Bet(cList, PN, screen):
    pass

def Raise(cList, PN, screen):
    pass

def Fold(cList, PN, screen):
    pass
    
def Decider(message, cList, PN, screen):
    if message == b'check':
        Check(cList, PN, screen)
    elif message == b'call':
        Call(cList, PN, screen)
    elif message == b'bet':
        Bet(cList, PN, screen)
    elif message == b'raise':
        Raise(cList, PN, screen)
    elif message == b'fold':
        Fold(cList, PN, screen)
    else:
        pass

    
        