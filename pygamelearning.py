import pygame,math
from pygame.locals import *

pygame.init()

displaySize = (600,800)

display = pygame.display.set_mode(displaySize)

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
pink = (255,200,200)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill(white)

    for i in range(3,4):
        pygame.draw.rect(display, green, [50*i,50*i,250,100])
        pygame.draw.rect(display, blue, [50*i,50*i,250,100])
        pygame.draw.ellipse(display,red,[50*i,50*i,250,100])
        
    pygame.draw.line(display, pink, (0,0), (250,100),3)

    pygame.draw.polygon(display,red,[(100,100),(0,200),(200,200),])
    pygame.draw.circle(display,pink, (300,300),50)
    pygame.draw.arc(display,green,[200,300,50,50], 0, math.pi,5)
    pygame.draw.lines(display,black, False,[(0,0),(30,50),(500,500),(350,40)], 4)

    pygame.display.update()