import pygame
import time
import os
import socket
from Card import Card
from Player import Player

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
numPlayers = 0
player1, player2, player3, player4, player5 = "", "", "", "", ""


class Poker():
    def __init__(self, screen):
        riverLocation1 = (screen.get_width()/2, screen.get_height()/10)
        riverLocation2 = (0, 0)
        riverLocation3 = (0, 0)
        Turn1Location = (0, 0)
        Turn2Location = (0, 0)
        Hand1Location = (0, 0)
        Hand2Location = (0, 0)

    def displayImage(self, location, screen, imageAddress, size):
        image = pygame.image.load(os.path.join(imageAddress))
        image = pygame.transform.scale(image.convert_alpha(), size)
        imageRect = image.get_rect()
        imageRect.center = location
        screen.blit(image, imageRect)
        pygame.display.flip()

    def initializeGame(self, screen):
        running = True
        while running == True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT: 
                    running = False
               
            self.last = pygame.time.get_ticks()
            displayText("Welcome to Poker", (screen.get_width()/2, screen.get_height()/2), screen, 80)
            displayText("Waiting for Players...", (screen.get_width()/2, screen.get_height()/2 + 50), screen, 80)
            
            pygame.display.update()

            # now = pygame.time.get_ticks()
            # while now - self.last <= 3000:
            #     now = pygame.time.get_ticks()
            
            print('hello boi')

            #Code to connect players
            s = socket.socket()
            port = 20000
            host = socket.gethostbyname(socket.gethostname())
            s.bind((host,port))
            s.listen(5)
            connectors = []

            previous = pygame.time.get_ticks()
            current = pygame.time.get_ticks()
            print("------WORK pls---------")
            
            s.settimeout(10)
            while True:
                try:
                    c, addr = s.accept()
                    print('got connection from', addr)

                    c.send('Tank you for connecting with your friendly neighborhood spiderman'.encode())
                    message = (c.recv(1024))
                    print (message)
                    connectors.append(addr)
                except socket.timeout as e:
                    break
            
            
            
            # try:
            #     if(current - previous <= 10000):
            #         connectors.append(askForConnection(s))
            #         current = pygame.time.get_ticks()
            # except:
            #     break
            
            # if(current - previous <= 10000):
            #     connectors.append(askForConnection(s))
            #     current = pygame.time.get_ticks()
            # if(current - previous <= 10000):
            #     print("On third guy and time is not up yet")
            #     connectors.append(askForConnection(s))
            #     current = pygame.time.get_ticks()
            # if(current - previous <= 10000):
            #     connectors.append(askForConnection(s))
            #     current = pygame.time.get_ticks()
            # if(current - previous <= 10000):
            #     connectors.append(askForConnection(s))
            #     current = pygame.time.get_ticks()   
                    
            
            # s.close
                

                
            #
            #
            numPlayers = len(connectors)

            #Drawing rects for river and turn card positions
            #
            #
            #
            screen.fill((34, 139, 34))

            #Drawing player avatars
            player1 = Player("Player 1", 1000, (110, screen.get_height()/6), (130, screen.get_height()/6))
            player2 = Player("Player 2", 1000, (110, 2*screen.get_height()/6), (130, 2*screen.get_height()/6))
            player3 = Player("Player 3", 1000, (110, 3*screen.get_height()/6), (130, 3*screen.get_height()/6))
            player4 = Player("Player 4", 1000, (110, 4*screen.get_height()/6), (130, 4*screen.get_height()/6))
            player5 = Player("Player 5", 1000, (110, 5*screen.get_height()/6), (130, 5*screen.get_height()/6))

            player1Loc = (110, screen.get_height()/6)
            player2Loc = (110, 2*screen.get_height()/6)
            player3Loc = (110, 3*screen.get_height()/6)
            player4Loc = (110, 4*screen.get_height()/6)
            player5Loc = (110, 5*screen.get_height()/6)

            player1TLoc = (130, screen.get_height()/6)
            player2TLoc = (130, 2*screen.get_height()/6)
            player3TLoc = (130, 3*screen.get_height()/6)
            player4TLoc = (130, 4*screen.get_height()/6)
            player5TLoc = (130, 5*screen.get_height()/6)

            players = [player1, player2, player3, player4, player5]

            for x in range (numPlayers):
                self.displayImage(players[x].getAvLoc(), screen, "avatar.png", (100, 100))
                displayText(players[x].getName(), players[x].getTextLoc(), screen, 40)

            pygame.display.update()
            print("displaying image")
            
            running = False
            
    def winnerCheck(self):
        return True

    def gameLoop(self, screen):
        running = True
        self.initializeGame(screen)
        while self.winnerCheck() == True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    quit()

            #Start Round






            


            pygame.display.update()
            clock.tick(100)
        
# def askForConnection(s):
#         c, addr = s.accept()
#         print('got connection from', addr)

#         c.send('Tank you for connecting with your friendly neighborhood spiderman'.encode())
#         message = (c.recv(1024))
#         print (message)
#         return addr


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


    startGame = False

    displayText("Click to Begin", (width/2, height/2), screen, 50)

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
    poker.gameLoop(screen)
main()


        






