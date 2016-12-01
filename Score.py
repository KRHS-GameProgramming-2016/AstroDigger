import pygame, sys, math 

class Score():
    def __init__(self, pos):
        self.value = 0
        self.font = pygame.font.Font()
        self.image = font.render("Score: " + str(self.value), True, (255,0,0))
        self.rect = self.image.rect
