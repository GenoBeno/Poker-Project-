import socket
import time
import pygame
import os
from Card import Card
from Player import Player
from pygame.locals import *


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
numPlayers = '0'
playerNum = '0'

player1, player2, player3, player4, player5 = "", "", "", "", ""
s = socket.socket()
port = 20000
s.connect(('137.112.230.61', port)) #Maxwell is currently hosting
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
            #Code to connect players
        
        #raisevalue = 0
        
        while running == True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT: 
                    running = False
               
            displayText("Welcome to Poker", (screen.get_width()/2, screen.get_height()/2), screen, 80,'white')
            displayText("Waiting for Players...", (screen.get_width()/2, screen.get_height()/2 + 50), screen, 80,'white')
            
            pygame.display.update()
            #'137.112.223.68' - Maxwell's IP
            #'137.112.224.150' - Dhiraj's IP
            string = int(s.recv(1024))
            
            
            pygame.display.update()
            
            

            
            

            

            
            

        

            playerNum = string % 10
            numPlayers = string // 10
            # numPlayers = string[:-2]
            # playerNum = string[-1:]
            # print(numPlayers)
            # print(playerNum)
            # while True:
            # playerNum = int(s.recv(1024))
                # break
            # print(str(numPlayers) + "gey")
            # print(str(playerNum) + " IM AKSJDFKLAJSDF")
            # pygame.display.update()
            # # print("displayed player number")
            

            screen.fill((34, 139, 34))
            displayText("You are Player " + str(playerNum), (screen.get_width()-200, screen.get_height()-50), screen, 50,'white')
            pygame.display.update()
            

            # screen.fill((34, 139, 34))

            #Drawing rects for flop, turn, river, and hand
            pygame.draw.rect(screen,(0,0,0),[screen.get_width()-210,90,105,105], 5)
            pygame.draw.rect(screen,(0,0,0),[screen.get_width()-375,90,105,105], 5)
            pygame.draw.rect(screen,(0,0,0),[screen.get_width()-540,90,105,105], 5)
            displayText("Flop",[screen.get_width()-323,40],screen, 60,'white')
            pygame.draw.line(screen, (255, 255, 255), (screen.get_width()-600, 75), (screen.get_width()-50, 75), 4)

            pygame.draw.rect(screen, (0, 0, 0), [screen.get_width()-460, 280, 105, 105], 5)
            pygame.draw.rect(screen, (0, 0, 0), [screen.get_width()-280, 280, 105, 105], 5)
            displayText("Turn", [screen.get_width()-410, 250], screen, 60,'white')

            displayText("River", [screen.get_width()-230, 250], screen, 60,'white')

            # pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-300,105,30])
            # pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-220,105,28])
            # pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-260,105,28])
            # pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-180,105,28])
            # pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-140,105,27])
            # displayText('Check', [screen.get_width()- 150,screen.get_height()- 285], screen, 40,'black')
            # displayText('Bet',[screen.get_width()-150,screen.get_height()-205], screen,40,'black')
            # displayText('Call',[screen.get_width()-150, screen.get_height() - 245],screen, 40,'black')
            # displayText('Raise',[screen.get_width()-150, screen.get_height()-165], screen,40,'black')
            # displayText('Fold',[screen.get_width()-150, screen.get_height()-125],screen,40,'black')
            

            
            

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
                displayText(players[x].getName(), players[x].getTextLoc(), screen, 40,'white')

            pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-300,105,30])
            pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-220,105,28])
            pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-140,105,27])
            pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-260,105,28])
            pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-180,105,28])
            displayText('Check', [screen.get_width()- 150,screen.get_height()- 285], screen, 40,'black')
            displayText('Bet',[screen.get_width()-150,screen.get_height()-205], screen,40,'black')
            displayText('Fold',[screen.get_width()-150, screen.get_height()-125],screen,40,'black')
            displayText('Call',[screen.get_width()-150, screen.get_height() - 245],screen, 40,'black')
            displayText('Raise',[screen.get_width()-150, screen.get_height()-165], screen,40,'black')
            displayText('Press 1',[screen.get_width()-270,screen.get_height()-285],screen,40, 'white')
            displayText('Press 3',[screen.get_width()-270,screen.get_height()-205],screen,40, 'white')
            displayText('Press 5',[screen.get_width()-270,screen.get_height()-125],screen,40, 'white')
            displayText('Press 2',[screen.get_width()-270,screen.get_height()-245],screen,40,'white')
            displayText('Press 4',[screen.get_width()-270,screen.get_height()-165],screen,40,'white')

            
            

            pygame.display.update()
            print("displaying image")
            
            
            # pygame.time.delay(5000)
            # print("rarded")
            # pygame.draw.rect(screen, (34, 139, 34), [screen.get_width()/2-500, screen.get_height()/2-100, 750, 300])
            pygame.display.update()

            running = False
        #message = s.recv(2048)
            
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
        
        
            def firstturn():
                follcheck()
                pygame.display.update()
                

            def middleturn():
                print('middleturnstart')
                while True:
                    message2 = s.recv(1024)
                    if message2 == (b'check'):
                        follcheck()
                        break
                    elif message2 == (b'bet'):
                        follbet()
                        break
                    elif message2 == (b'call'):
                        print('callworked')
                        follcall()
                        break
                    elif message2 == (b'raise'):
                        follraise()
                        break
                    elif message2 == (b'fold'):
                        follfold()
                        break 

            def follcheck():
                while True:
                    events = pygame.event.get()
                    for event in events:
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            print('it quit')
                        if event.type == pygame.KEYDOWN:
                            if(event.key == pygame.K_1):     #checks
                                s.send('check'.encode())
                                print('it checked')
                                break
                            elif(event.key == pygame.K_3):   #bets
                                #display bet amounts on boxes
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-300,105,30])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-260,105,28])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-220,105,28])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-180,105,28])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-140,105,27])
                                displayText('Add 10',[screen.get_width()-150, screen.get_height() - 285],screen, 33,'red')
                                displayText('Add 50',[screen.get_width()-150, screen.get_height()-245], screen,33,'red')
                                displayText('Add 100',[screen.get_width()-150, screen.get_height()-205],screen,33,'red')
                                pygame.display.update()
                                bet = 0
                                
                                while True:
                                    events = pygame.event.get()
                                    for event in events:
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            print('it quit')
                                        if event.type == pygame.KEYDOWN:    
                                            if(event.key == pygame.K_1):
                                                bet += 10
                                                print('added 10')
                                            if(event.key == pygame.K_2):
                                                bet = bet + 50
                                                print('added 50')
                                            if(event.key == pygame.K_3):
                                                bet += 100
                                                print('added 100')
                                            if(event.key == pygame.K_KP_ENTER):
                                                print('pressed enter')
                                                s.send('bet'.encode())
                                                s.send(str(bet).encode())
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-300,105,30])
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-220,105,28])
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-140,105,27])
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-260,105,28])
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-180,105,28])
                                                displayText('Check', [screen.get_width()- 150,screen.get_height()- 285], screen, 40,'black')
                                                displayText('Bet',[screen.get_width()-150,screen.get_height()-205], screen,40,'black')
                                                displayText('Fold',[screen.get_width()-150, screen.get_height()-125],screen,40,'black')
                                                displayText('Call',[screen.get_width()-150, screen.get_height() - 245],screen, 40,'black')
                                                displayText('Raise',[screen.get_width()-150, screen.get_height()-165], screen,40,'black')
                                                pygame.display.update()
                                                break
                                        
                            elif(event.key == pygame.K_5):   #folds
                                s.send('fold'.encode())
                                break

            def follcall():
                #display call,raise,fold
                while True:
                    events = pygame.event.get()
                    for event in events:
                        if event.type == pygame.QUIT:
                            pygame.quit
                        if event.type == pygame.KEYDOWN:
                            if(event.key == pygame.K_2):   #calls
                                s.send('call'.encode())
                                break
                            elif(event.key == pygame.K_4):   #raises
                                        #display raisevalue amounts on boxes
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-300,105,30])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-260,105,28])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-220,105,28])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-180,105,28])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-140,105,27])
                                displayText('Add 10',[screen.get_width()-150, screen.get_height() - 285],screen, 33,'red')
                                displayText('Add 50',[screen.get_width()-150, screen.get_height()-245], screen,33,'red')
                                displayText('Add 100',[screen.get_width()-150, screen.get_height()-205],screen,33,'red')
                                pygame.display.update()
                                raisevalue = 0
                                while True:
                                    events = pygame.event.get()
                                    for event in events:
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                        if event.type == pygame.KEYDOWN:
                                            if(event.key == pygame.K_1):
                                                raisevalue + 10
                                                print('added 10')
                                            if(event.key == pygame.K_2):
                                                raisevalue + 50
                                                print('added 50')
                                            if(event.key == pygame.K_3):
                                                raisevalue +100
                                                print('added 100')
                                            if(event.key == pygame.K_KP_ENTER):
                                                s.send('raise'.encode())
                                                s.send(str(raisevalue).encode())
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-300,105,30])
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-220,105,28])
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-140,105,27])
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-260,105,28])
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-180,105,28])
                                                displayText('Check', [screen.get_width()- 150,screen.get_height()- 285], screen, 40,'black')
                                                displayText('Bet',[screen.get_width()-150,screen.get_height()-205], screen,40,'black')
                                                displayText('Fold',[screen.get_width()-150, screen.get_height()-125],screen,40,'black')
                                                displayText('Call',[screen.get_width()-150, screen.get_height() - 245],screen, 40,'black')
                                                displayText('Raise',[screen.get_width()-150, screen.get_height()-165], screen,40,'black')
                                                pygame.display.update()
                                                break
                            elif(event.key == pygame.K_5):      #folds
                                s.send('fold'.encode())
                                break

            def follraise():
                #display call, raise, fold
                while True:
                    events = pygame.event.get()
                    for event in events:
                        if event.type == pygame.QUIT:
                            pygame.quit
                        if event.type == pygame.KEYDOWN:
                            if(event.key == pygame.K_2):   #calls
                                s.send('call'.encode())
                                break
                            elif(event.key == pygame.K_4):   #raises
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-300,105,30])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-260,105,28])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-220,105,28])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-180,105,28])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-140,105,27])
                                displayText('Add 10',[screen.get_width()-150, screen.get_height() - 285],screen, 33,'red')
                                displayText('Add 50',[screen.get_width()-150, screen.get_height()-245], screen,33,'red')
                                displayText('Add 100',[screen.get_width()-150, screen.get_height()-205],screen,33,'red')
                                pygame.display.update()
                                raisevalue = 0
                                
                                while True:
                                    events = pygame.event.get()
                                    for event in events:
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                        if event.type == pygame.KEYDOWN:
                                            if(event.key == pygame.K_1):
                                                raisevalue + 10
                                            if(event.key == pygame.K_2):
                                                raisevalue + 50
                                            if(event.key == pygame.K_3):
                                                raisevalue +100
                                            if(event.key == pygame.K_KP_ENTER):
                                                s.send(str('raise').encode())
                                                s.send(str(raisevalue).encode())
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-300,105,30])
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-220,105,28])
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-140,105,27])
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-260,105,28])
                                                pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-180,105,28])
                                                displayText('Check', [screen.get_width()- 150,screen.get_height()- 285], screen, 40,'black')
                                                displayText('Bet',[screen.get_width()-150,screen.get_height()-205], screen,40,'black')
                                                displayText('Fold',[screen.get_width()-150, screen.get_height()-125],screen,40,'black')
                                                displayText('Call',[screen.get_width()-150, screen.get_height() - 245],screen, 40,'black')
                                                displayText('Raise',[screen.get_width()-150, screen.get_height()-165], screen,40,'black')
                                                pygame.display.update()
                                                break
                            elif(event.key == pygame.K_5):      #folds
                                s.send('fold'.encode())
                                break
            def follbet():
                #display call,raise,fold
                while True:
                    events = pygame.event.get()
                    for event in events:
                        if event.type == pygame.QUIT:
                            pygame.quit
                        if event.type == pygame.KEYDOWN:
                            if(event.key == pygame.K_2):   #calls
                                s.send('call'.encode())
                                break
                            elif(event.key == pygame.K_4):   #raises
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-300,105,30])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-260,105,28])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-220,105,28])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-180,105,28])
                                pygame.draw.rect(screen,(0,0,0),[screen.get_width()-200, screen.get_height()-140,105,27])
                                displayText('Add 10',[screen.get_width()-150, screen.get_height() - 285],screen, 33,'red')
                                displayText('Add 50',[screen.get_width()-150, screen.get_height()-245], screen,33,'red')
                                displayText('Add 100',[screen.get_width()-150, screen.get_height()-205],screen,33,'red')
                                pygame.display.update()
                                raisevalue = 0
                                
                                while True:
                                    events = pygame.event.get()
                                    for event in events:
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                        if event.type == pygame.KEYDOWN:
                                            if(event.key == pygame.K_1):
                                                    raisevalue + 10
                                            if(event.key == pygame.K_2):
                                                    raisevalue + 50
                                            if(event.key == pygame.K_3):
                                                    raisevalue +100
                                            if(event.key == pygame.K_KP_ENTER):
                                                    s.send(str('raise').encode())
                                                    s.send(str(raisevalue).encode())
                                                    pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-300,105,30])
                                                    pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-220,105,28])
                                                    pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-140,105,27])
                                                    pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-260,105,28])
                                                    pygame.draw.rect(screen,(255,0,0),[screen.get_width()-200, screen.get_height()-180,105,28])
                                                    displayText('Check', [screen.get_width()- 150,screen.get_height()- 285], screen, 40,'black')
                                                    displayText('Bet',[screen.get_width()-150,screen.get_height()-205], screen,40,'black')
                                                    displayText('Fold',[screen.get_width()-150, screen.get_height()-125],screen,40,'black')
                                                    displayText('Call',[screen.get_width()-150, screen.get_height() - 245],screen, 40,'black')
                                                    displayText('Raise',[screen.get_width()-150, screen.get_height()-165], screen,40,'black')
                                                    pygame.display.update()
                                                    break
                            elif(event.key == pygame.K_5):      #folds
                                s.send('fold'.encode())
                                break


            


            pygame.display.update()
            while True:
                
                message = s.recv(2048)
                print(message)
                if message == (b'firstup'):
                    print('try')
                    firstturn()
                    break
                if message == (b'next'):
                    middleturn()
                    print('middleturndone')
            clock.tick(100)
        

    # def newRound(self, screen):


def displayText(text, location, screen, fontSize, color):
    TNRFont = pygame.font.SysFont("Crimson-Roman.ttf", fontSize)
    textSurface = TNRFont.render(str(text), True, pygame.Color(color))
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

    displayText("Click to Begin", (width/2, height/2), screen, 50,'white')

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
