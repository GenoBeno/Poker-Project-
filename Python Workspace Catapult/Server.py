import pygame
import time
import socket
pygame.init()

# s = socket.socket()
# port = 20000
# host = socket.gethostbyname(socket.gethostname())
# s.bind((host,port))
# s.listen(5)
# connectors = []


# print("AKJSHDFKJASHKDFJASHDJKFSJK")
# s.settimeout(10)
# while True:
#     try:
#         c, addr = s.accept()
#         print('got cnection from', addr)

#         # c.send('Tank you for connecting with your friendly neighborhood spiderman'.encode())
#         # message = (c.recv(1024))
#         # print (message)
#         connectors.append(c)
#     except socket.timeout as e:
#         break

# numPlayers = len(connectors)
# for x in range (numPlayers):
#     connectors[x].send(str(numPlayers).encode())

# def playerStanding():
    
        
def assignRoundPoints(q,w,e,r,t,y,u):
    bards=[q,w,e,r,t,y,u]
    cardValue=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
    dict = {"pair":1, "two-pair":2, "three-of-a-kind":3, "flush":4, "full-house":5, "four-of-a-kind":6, "straight-flush":7, "royal-flush":8}
    cardValues = {"Ace":1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace14": 14}
    global susAsFuck=[]

#  for x in range(cardValue):
    #  bards.count(cardValue[x])

    FHdict = {}
    checker = []
    for card in bards:
        if FHdict[card.getValue()] == None:
            FHdict[card.getValue()] = 1
        else:
            FHdict[card.getValue()] = FHdict[card.getValue()] + 1

    if 3 in list(FHdict.values()) and 2 in list(FHdict.values()):
        #FULL HOUSE MOTHAFUCKA
    if list(FHdict).count(2)==2:
        return 2
    if 2 in list(FHdict.values()):
       return 1
    if 3 in list(FHdict.values()):
        return 3
    if 4 in list(FHdict.values()):
        #four of a kind
    
    
    
    if susAsFuck[0]==10 and flush(susAsFuck)==True and straight(susAsFuck):
        return 99999999
    elif straight(cards) 
      return 4
    elif 
    
    else 
    return 0

    def detectWin()
        
    #straight flush if flush && straight
    #royal flush if flush && straight && 



                    
def straight(cards):
    
    y=0
    yeetOnMeat= True
for x in bards: 
    checker.append(cardValues[x.getValue()])
checker.sort() 
for x in range(len(checker)-1):
    if checker[x+1]-1==checker[x] and y<=5:
        susAsFuck.append(x)
        y+=1
    else:
        return not yeetOnMeat
    

def flush(bards):
    tolerance=2
    for x in range(len(bards)-1):
        if bards[x].getSuitValue()!=bards[x+1].getSuitValue():
            tolerance+=1
    if tolerance<=2:
        return true




card1 = Card("A", "Hearts", "asdf")
card2 = Card("A", "Clubs", "asdf")
card3 = Card("A", "Diamonds", "Asdf")
card4 = Card("2", "Spades", "asdf")
card5 = Card("2", "Clubs", "asdf")
card6 = Card("3", "Hearts", "asdf")
card7 = Card("4", "Spades", "asdf")




print(assignRoundPoints(card1, card2, card3, card4, card5, card6, card7))
    
    

print ("hello me gay")


