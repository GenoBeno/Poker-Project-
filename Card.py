import pygame
import time
from random import randint

cardValue=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
suitValue=['Hearts','Diamonds','Spades','Clubs']
imageNames=['2_of_clubs.png','2_of_diamonds.png','2_of_hearts.png','2_of_spades.png','3_of_clubs.png','3_of_diamonds.png','3_of_hearts.png','3_of_spades.png','4_of_clubs.png','4_of_diamonds.png','4_of_hearts.png','4_of_spades.png','5_of_clubs.png','5_of_diamonds.png','5_of_hearts.png','5_of_spades.png',
        '6_of_clubs.png','6_of_diamonds.png','6_of_hearts.png','6_of_spades.png','7_of_clubs.png','7_of_diamonds.png','7_of_hearts.png','7_of_spades.png','8_of_clubs.png','8_of_diamonds.png','8_of_hearts.png','8_of_spades.png','9_of_clubs.png','9_of_diamonds.png','9_of_hearts.png','9_of_spades.png','10_of_clubs.png','10_of_diamonds.png','10_of_hearts.png',
        '10_of_spades.png','ace_of_clubs.png','ace_of_diamonds.png','ace_of_hearts.png','ace_of_spades.png','queen_of_clubs2.png','queen_of_diamonds2.png','queen_of_hearts2.png','queen_of_spades2.png','jack_of_clubs2.png','jack_of_diamonds2.png','jack_of_hearts2.png','jack_of_spades2.png','king_of_clubs2.png','king_of_diamonds2.png','king_of_hearts2.png','king_of_spades2.png']

pygame.init()

class Card():
    def __init__(self, value, suit, imageName):
        self.cardValue = value
        self.suitValue = suit
        self.imageAddress = imageName
    
    def getCardValue(self):
        return self.cardValue

    def getSuitValue(self):
        return self.suitValue

    def displayCardImage(location):
        image = pygame.image.load(os.path.join(self.imageAddress))
        image = pygame.transform.scale(image.convert_alpha(), (100, 100))
        screen.blit(location)
        pygame.display.flip()
    
    def createDeck():
        e=0
        i = 0
        deck=[]
        for val in range(len(cardValue)):
            for suit in range(len(suitValue)):
                
                deck.append(Card(cardValue[val],suitValue[suit],imageNames[i]))
                i+=1
                    
        return deck

    def shuffleDeck(u):
        shuffledDeck=[]
        for i in range(0,len(u)):
            n=randint(0,len(u)-1)
            shuffledDeck.append(u[n])
            print(u[n])
        return shuffledDeck

    def __str__(self):
        return str(self.cardValue) + " of " + str(self.suitValue)

    def deckToString(deck):
        fetusDeletus=""
        for g in range(len(deck)):
                fetusDeletus+= str(deck[g]) + " "
        return fetusDeletus

    def getImageAddress(self):
        return self.imageAddress
            
    
        
        
            

# card = Card("7", "Hearts", "7_of_hearts.png")
# #print(card)
# antony=Card.createDeck()
# #print("hi"+"\n"+"hi")


# g=Card.createDeck()
# Card.shuffleDeck(g)
