import pygame
import time
import os
from Card import Card
from random import *

pygame.init()

cardValue=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
suitValue=['Hearts','Diamonds','Spades','Clubs']
imageNames=['2_of_clubs.png','2_of_diamonds.png','2_of_hearts.png','2_of_spades.png','3_of_clubs.png','3_of_diamonds.png','3_of_hearts.png','3_of_spades.png','4_of_clubs.png','4_of_diamonds.png','4_of_hearts.png','4_of_spades.png','5_of_clubs.png','5_of_diamonds.png','5_of_hearts.png','5_of_spades.png',
       '6_of_clubs.png','6_of_diamonds.png','6_of_hearts.png','6_of_spades.png','7_of_clubs.png','7_of_diamonds.png','7_of_hearts.png','7_of_spades.png','8_of_clubs.png','8_of_diamonds.png','8_of_hearts.png','8_of_spades.png','9_of_clubs.png','9_of_diamonds.png','9_of_hearts.png','9_of_spades.png','10_of_clubs.png','10_of_diamonds.png','10_of_hearts.png',
       '10_of_spades.png','ace_of_clubs.png','ace_of_diamonds.png','ace_of_hearts.png','ace_of_spades.png','queen_of_clubs2.png','queen_of_diamonds2.png','queen_of_hearts2.png','queen_of_spades2.png','jack_of_clubs2.png','jack_of_diamonds2.png','jack_of_hearts2.png','jack_of_spades2.png','king_of_clubs2.png','king_of_diamonds2.png','king_of_hearts2.png','king_of_spades2.png']

class Deck():
    # def __init__(self, screen):
    #     self.window = screen
    #     self.deck = shuffleDeck(createDeck())
    def __init__(self):
        self.deck = self.shuffleDeck(self.createDeck())

    def createDeck(self):
       i = 0
       deck=[]
       for val in range(len(cardValue)):
           for suit in range(len(suitValue)):  
                deck.append(Card(cardValue[val],suitValue[suit],imageNames[i]))
                i+=1
                  
       return deck
         

    def shuffleDeck(self, deck):
       shuffledDeck=[]
       for i in range(0,len(deck)):
           n=randint(0,len(deck)-1)
           shuffledDeck.append(deck[n])
       return shuffledDeck

    def getDeck(self):
        return self.deck

    def getTopCard(self):
        return self.deck.pop()





    