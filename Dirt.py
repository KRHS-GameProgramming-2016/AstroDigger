import pygame, sys, math

class Wall():
    def __init__(self, pos=[0,0], size=None):
        self.image = pygame.image.load("AstroDigger/Resoucres/Dirt/Dirt For Level 1.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
    def __init__(self, pos=[0,0], size=None):
        self.image = pygame.image.load("AstroDigger/Resoucres/Dirt/Dirt For Level 2.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
    def __init__(self, pos=[0,0], size=None):
        self.image = pygame.image.load("AstroDigger/Resoucres/Dirt/Dirt For Level 3.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
    def __init__(self, pos=[0,0], size=None):
        self.image = pygame.image.load("AstroDigger/Resoucres/Dirt/Dirt For Level 4.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
    def __init__(self, pos=[0,0], size=None):
        self.image = pygame.image.load("AstroDigger/Resoucres/Dirt/Dirt For Level 5.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
