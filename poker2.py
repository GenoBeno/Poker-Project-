import pygame
import time
import os
from Card import Card
import pygame
import time
from random import randint

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

riverLocation1 = (0, 0)
riverLocation2 = (0, 0)
riverLocation3 = (0, 0)
Turn1Location = (0, 0)
Turn2Location = (0, 0)
Hand1Location = (0, 0)
Hand2Location = (0, 0)

class Poker():

   def __init__(self, screen):
       riverLocation1 = (screen.get_width()/2, screen.get_height()/10)
       riverLocation2 = (0, 0)
       riverLocation3 = (0, 0)
       Turn1Location = (0, 0)
       Turn2Location = (0, 0)
       Hand1Location = (0, 0)
       Hand2Location = (0, 0)

   def initializeGame(self, screen):
       running = True
       while running == True:
           events = pygame.event.get()
           for event in events:
               if event.type == pygame.QUIT:
                   running = False

           print("initialize game called")
           self.last = pygame.time.get_ticks()
           displayText("Welcome to Poker", (screen.get_width()/2, screen.get_height()/2), screen, 80)
           displayText("Waiting for Players...", (screen.get_width()/2, screen.get_height()/2 + 50), screen, 80)
          
           pygame.display.update()

           now = pygame.time.get_ticks()
           while now - self.last <= 500:
               now = pygame.time.get_ticks()
              
           screen.fill((34, 139, 34))

           #Code to check that all players have connected
           pygame.draw.rect(screen,(0,0,0),[screen.get_width()-110,90,105,105], 5)
           pygame.draw.rect(screen,(0,0,0),[screen.get_width()-225,90,105,105], 5)
           pygame.draw.rect(screen,(0,0,0),[screen.get_width()-340,90,105,105], 5)
           displayText("Anthony is a flop",[screen.get_width()-173,60],screen, 80)
           #displayImage([screen.get_width()-57.5,142], screen, 'king_of_hearts2.png', (100,100))
           #displayImage([screen.get_width()-172.5,142], screen, 'king_of_spades2.png', (100,100))
           #displayImage([screen.get_width()-287.5,142], screen, 'king_of_diamonds2.png', (100,100))
           t= Card.createDeck()
           Card.shuffleDeck(t)

           drawFlopStraight(t,screen)
           pygame.display.update()
           
           #
           #

           #Drawing rects for river and turn card positions
           now = pygame.time.get_ticks()
           self.last = pygame.time.get_ticks()
           while now - self.last <= 5000:
                now = pygame.time.get_ticks()
           

           
           running = False
          
   def winnerCheck(self):
       return True

   def gameLoop(self, screen):
       running = True
       self.initializeGame(screen)
       while running == True:
           events = pygame.event.get()
           for event in events:
               if event.type == pygame.QUIT:
                   running = False

          
          


           pygame.display.update()
           clock.tick(100)
      

def displayText(text, location, screen, fontSize):
   TNRFont = pygame.font.SysFont("Crimson-Roman.ttf", fontSize)
   textSurface = TNRFont.render(str(text), True, pygame.Color(255, 255, 255))
   textRect = textSurface.get_rect()

   textRect.center = location
   screen.blit(textSurface, textRect)

def main():
   displayObject = pygame.display.Info()

   width = displayObject.current_w-400
   height = displayObject.current_h-300

   screen = pygame.display.set_mode((width, height))
   screen.fill((34, 139, 34))
   pygame.display.set_caption("Texas Hold-em Poker")
   e=Card.createDeck() 

   


   startGame = False

   displayText("Click to Begin", (width/2, height/2), screen, 50)
   drawRiverRandom(e,3,screen)


   while not startGame:
       events = pygame.event.get()
       for event in events:
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               screen.fill((34, 139, 34))
               startGame = True
       pygame.display.update()
  
   poker = Poker(screen)
   # displayText("River", riverLocation1, screen)
   # Card("King", "Clubs", "king_of_clubs.png").displayCardImage(riverLocation1, screen)
   # poker.initializeGame(screen)
#    poker.gameLoop(screen)

def displayImage(location, screen, imageAddress, size):
       image = pygame.image.load(os.path.join(imageAddress))
       image = pygame.transform.scale(image.convert_alpha(), size)
       imageRect = image.get_rect()
       imageRect.center = location
       screen.blit(image, imageRect)
       pygame.display.flip()

def drawRiverRandom(deck,f,ree):
    n=randint(0,51)
    c=142
    e=57.5
    d=115
    if f==0:
        return 
    elif f<=3:
        displayImage([ree.get_width()-287.5+((f-1)*d),c], ree, deck[n].getImageAddress(), (100,100))
        deck.remove(deck[n])
        drawRiverRandom(deck,f-1,ree)

def getFlopCards()
    return currentFlop
    
def drawFlopStraight(shuffledDeck,ree):
    CARDHEIGHT=142
    CARDOFF=15
    global currentFlop= []
    x=0
    while x<=2:
        displayImage([ree.get_width()-287+(115*(x)),142], ree, shuffledDeck[x].getImageAddress(), (100,100))
        x += 1
        currentFlop+=shuffledDeck[x]



def newRound:

def winConditions()
    




cardValue=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
suitValue=['Hearts','Diamonds','Spades','Clubs']
imageNames=['2_of_clubs.png','2_of_diamonds.png','2_of_hearts.png','2_of_spades.png','3_of_clubs.png','3_of_diamonds.png','3_of_hearts.png','3_of_spades.png','4_of_clubs.png','4_of_diamonds.png','4_of_hearts.png','4_of_spades.png','5_of_clubs.png','5_of_diamonds.png','5_of_hearts.png','5_of_spades.png',
        '6_of_clubs.png','6_of_diamonds.png','6_of_hearts.png','6_of_spades.png','7_of_clubs.png','7_of_diamonds.png','7_of_hearts.png','7_of_spades.png','8_of_clubs.png','8_of_diamonds.png','8_of_hearts.png','8_of_spades.png','9_of_clubs.png','9_of_diamonds.png','9_of_hearts.png','9_of_spades.png','10_of_clubs.png','10_of_diamonds.png','10_of_hearts.png',
        '10_of_spades.png','ace_of_clubs.png','ace_of_diamonds.png','ace_of_hearts.png','ace_of_spades.png','queen_of_clubs2.png','queen_of_diamonds2.png','queen_of_hearts2.png','queen_of_spades2.png','jack_of_clubs2.png','jack_of_diamonds2.png','jack_of_hearts2.png','jack_of_spades2.png','king_of_clubs2.png','king_of_diamonds2.png','king_of_hearts2.png','king_of_spades2.png']

pygame.init()



    
        



        

main()
