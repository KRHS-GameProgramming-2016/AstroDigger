import pygame, sys, math, time
from Score import *

class LevelNumber(Score):
    def __init__(self, pos):
        Score.__init__(self, pos)
        self.startTime = time.clock()
        self.image = self.font.render("Level " + str(self.value + 1), True, (0,255,0))
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self, levelNumber):
        newValue = levelNumber
        if newValue != self.value:
            self.value = newValue
            self.image = self.font.render("Level " + str(self.value), True, (0,255,0))
            self.rect = self.image.get_rect(center = self.rect.center)


