import pygame

pygame.init()

running = True


# displayObject = pygame.display.Info()

# width = displayObject.current_w-400
# height = displayObject.current_h-300

#screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((600, 600))
screen.fill((34, 139, 34))
pygame.display.set_caption("Texas Holem-em Poker")

while running == True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: 
            running = False
    pygame.display.update()

