import pygame
import time
import os

pygame.init()

class Card():
    def __init__(self, value, suit, imageName):
        self.cardValue = value
        self.suitValue = suit
        self.imageAddress = imageName
    
    def getCardValue(self):
        return self.cardValue

    def getSuitValue(self):
        return self.suitValue

    def getImageAddress(self):
        return self.imageAddress

    def displayCardImage(self, location, screen):
        image = pygame.image.load(os.path.join(self.imageAddress))
        image = pygame.transform.scale(image.convert_alpha(), (100, 100))
        screen.blit(image, location)
        pygame.display.flip()


    




