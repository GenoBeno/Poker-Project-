import pygame
import time
import socket

pygame.init()

s = socket.socket()
port = 20000
host = socket.gethostbyname(socket.gethostname())
s.bind((host,port))
s.listen(5)
connectors = []


print("AKJSHDFKJASHKDFJASHDJKFSJK")
s.settimeout(10)
while True:
    try:
        c, addr = s.accept()
        print('got cnection from', addr)

        # c.send('Tank you for connecting with your friendly neighborhood spiderman'.encode())
        # message = (c.recv(1024))
        # print (message)
        connectors.append(c)
    except socket.timeout as e:
        break

numPlayers = len(connectors)
for x in range (numPlayers):
    connectors[x].send(str(numPlayers).encode())

def playerStanding():
    
        
def detectWin(q,w,e,r,t,y,u):
    bards=[q,w,e,r,t,y,u]
    RF=1
    SF=2
    FK=3
    FH=4
    F=5
    S=6
    TK=7
    TP=8
    P=9
    H=10
    for x in range(len(bards)):
        for f in range(len(bards))
            b=0
            if(bards[x].getValue()==bards[f].getValue())
            b=b+1






    
    

print ("hello me gay")


