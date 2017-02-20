import pygame, sys, math, time
from Score import *

class Lives(Score):
    def __init__(self, pos):
        Score.__init__(self, pos)
        self.startTime = time.clock()
        
        self.oneLifeImage = pygame.image.load("Resources/Lives/hearts1life.png")
        self.twoLivesImage = pygame.image.load("Resources/Lives/hearts2lives.png")
        self.threeLivesImage = pygame.image.load("Resources/Lives/hearts3lives.png")
        self.fourLivesImage = pygame.image.load("Resources/Lives/hearts4lives.png")
        self.fiveLivesImage = pygame.image.load("Resources/Lives/hearts5lives.png")
        
        self.image = self.fiveLivesImage
        self.rect = self.image.get_rect(center = self.rect.center)
        self.value = 5

    def update(self, playerLives):
        newValue = playerLives
        if newValue != self.value:
            self.value = newValue
            if self.value == 5:
                self.image = self.fiveLivesImage
            if self.value == 4:
                self.image = self.fourLivesImage
            if self.value == 3:
                self.image = self.threeLivesImage
            if self.value == 2:
                self.image = self.fourLivesImage
            if self.value == 1:
                self.image = self.oneLifeImage
            self.rect = self.image.get_rect(center = self.rect.center)


