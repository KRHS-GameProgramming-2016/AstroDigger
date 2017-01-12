import pygame, sys, math

class Dirt():
    def __init__(self, kind, pos=[0,0], size=None):
        self.image = pygame.image.load("Resources/Dirt/Dirt For Level " + kind + ".png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
        self.hp = int(kind)
        self.isDug = False
