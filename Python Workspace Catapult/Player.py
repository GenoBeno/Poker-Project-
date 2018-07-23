import pygame
import time
import os

pygame.init()

class Player():
    def __init__(self, n, amt, avLoc, tLoc):
        self.amount = amt #the amount of money the player has
        self.avatarLoc = avLoc
        self.textLoc = tLoc
        self.name = n
    
    def getAmount(self):
        return self.amount

    def getAvLoc(self):
        return self.avatarLoc

    def getTextLoc(self):
        return self.textLoc

    def setCards(self, card1, card2):
        self.cardOne = card1
        self.cardTwo = card2

    def getCard1(self):
        return self.cardOne

    def getCard2(self):
        return self.cardTwo

    def getName(self):
        return self.name
    def bet(self,amount#the amount the player wants to b e t)
        self.amount-=amount
        pot=pot+amount
    def disNiggaActuallyWon(self)
        self.amount=pot+self.amount   
        
    

    