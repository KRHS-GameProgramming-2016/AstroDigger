import pygame, sys, math, time
from Score import *

class Lives(Score):
    def __init__(self, pos):
        Score.__init__(self, pos)
        self.startTime = time.clock()
        self.image = self.font.render("Lives: " + str(self.value), True, (255,0,0))
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self, playerLives):
        newValue = playerLives
        if newValue != self.value:
            self.value = newValue
            self.image = self.font.render("Lives: " + str(self.value), True, (255,0,0))
            self.rect = self.image.get_rect(center = self.rect.center)


