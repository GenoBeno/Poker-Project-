import pygame
import time

pygame.init()
clock = pygame.time.Clock()
#pygame.setFill("white")

x = 0
y = 100
width = 100
height = 100

screenW = 500
screenH = 500
screen = pygame.display.set_mode((screenW, screenH))

screen.fill((255, 255, 255))

#rect = pygame.Rect(10, 300, 150, 150)

#pygame.draw.rect(screen, (0, 0, 0), rect)

#rect.fill(0, 0, 0)
#rect.setFill("black")
running = True
while(running):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: 
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if(x >= 15):
            x -= 9
            #pygame.time.delay(500)
            x -= 3
            #pygame.time.delay(500)
            x -= 2
            #pygame.time.delay(500)
            x -= 1

    if keys[pygame.K_RIGHT]:
        if(x <= screenW-15-width):
            x += 9
            # pygame.time.delay(500)
            x += 3
            # pygame.time.delay(500)
            x += 2
            # pygame.time.delay(500)
            x += 1

    if keys[pygame.K_UP]:
        if(y >= 15):
            y -= 9
            # pygame.time.delay(500)
            y -= 3
            # pygame.time.delay(500)
            y -= 2
            # pygame.time.delay(500)
            y -= 1

    if keys[pygame.K_DOWN]:
        if(y <= screenH-15-height):
            y += 9
            # pygame.time.delay(500)
            y += 3
            # pygame.time.delay(500)
            y += 2
            # pygame.time.delay(500)
            y += 1

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))       
    pygame.display.update()
    clock.tick(100)
    