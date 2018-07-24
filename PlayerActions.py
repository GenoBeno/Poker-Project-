import pygame


def follcheck():
    #display 3 options on boxes
    pygame.display.update()
    for event in events:
        if event.type == pygame.QUIT:
                pygame.quit
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_1):     #checks
                s.send('check'.encode())
                break
            elif(event.key == pygame.K_3):   #bets
                for bet in range[500]:
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
                    
                    if(event.key == pygame.K_1):
                        bet + 10
                    if(event.key == pygame.K_2):
                        bet + 50
                    if(event.key == pygame.K_3):
                        bet +100
                    if(event.key == pygame.K_KP_ENTER):
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

def follbet():
    #display call,raise,fold
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_2):   #calls
                s.send('call'.encode())
                break
            elif(event.key == pygame.K_4):   #raises
                for raisevalue in range[500]:
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

def follcall():
    #display call,raise,fold
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_2):   #calls
                s.send('call'.encode())
                break
            elif(event.key == pygame.K_4):   #raises
                for raisevalue in range[500]:
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
                        
                        if(event.key == pygame.K_1):
                            raisevalue + 10
                        if(event.key == pygame.K_2):
                            raisevalue + 50
                        if(event.key == pygame.K_3):
                            raisevalue +100
                        if(event.key == pygame.K_KP_ENTER):
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
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_2):   #calls
                s.send('call'.encode())
                break
            elif(event.key == pygame.K_4):   #raises
                for raisevalue in range[500]:
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

def firstturn:
    follcheck()
    pygame.display.update()

def middleturn():
    while True:
        
        if message == (b'check'):
            follcheck()
            break
        if message == (b'bet'):
            follbet()
            break
        if message == (b'call'):
            follcall()
            break
        if message == (b'raise'):
            follraise()
            break
        if message == (b'fold'):
            follfold()
            break
        