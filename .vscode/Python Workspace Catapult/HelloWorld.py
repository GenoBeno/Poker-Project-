import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((500, 500))

ballImage = pygame.transform.scale(pygame.image.load("D:/ball.png").convert(), (500, 500))

screen.blit(ballImage, (0, 0))

pygame.display.flip()

running = True

#colorList = [red, blue, green, yellow]
#index = 0

while (running):
    #if(index == 4):
   #     index = 0
    screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    #index+=1
    #screen.blit(ballImage, (10, 10))
    #font = pygame.font.Font('D:/COMIC', 30)
    #text = font.render("Good Old Epilepsy", True, 'black')
    #screen.blit(text, (1000, 500))
    pygame.display.update()


