import pygame
import time
import os

pygame.init()

class Player():
    def __init__(self, n, amt, scrn):
        self.amount = amt
        self.name = n
        self.screen = scrn
        # self.connRef = connectRef
    
    def getAmount(self):
        return self.amount

    def getAvLoc(self):
        if self.name == "Player 1":
            return (110, self.screen.get_height()/6)
        if self.name == "Player 2":
            return (110, 2*self.screen.get_height()/6)
        if self.name == "Player 3":    
            return (110, 3*self.screen.get_height()/6)
        if self.name == "Player 4":    
            return (110, 4*self.screen.get_height()/6)
        if self.name == "Player 5":
            return (110, 5*self.screen.get_height()/6)

    def getTextLoc(self):
        if self.name == "Player 1":
            return (130, self.screen.get_height()/6)
        if self.name == "Player 2":
            return (130, 2*self.screen.get_height()/6)
        if self.name == "Player 3":    
            return (130, 3*self.screen.get_height()/6)
        if self.name == "Player 4":    
            return (130, 4*self.screen.get_height()/6)
        if self.name == "Player 5":
            return (130, 5*self.screen.get_height()/6)   

    def setCards(self, card1, card2):
        self.cardOne = card1
        self.cardTwo = card2

    def getCard1(self):
        return self.cardOne

    def getCard2(self):
        return self.cardTwo

    def getName(self):
        return self.name

    