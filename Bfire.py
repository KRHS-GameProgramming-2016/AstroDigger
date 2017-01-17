import pygame, math, sys

class Bfire():
    def __init__(self, speed=0, pos=[0,0], size=64):
        self.imageLeft = pygame.image.load("Beatbox Fire Bolt Left.png")
        self.imageRight = pygame.image.load("Beatbox Fire Bolt Right.png")
        self.imageUp = pygame.image.load("Beatbox Fire Bolt Up.png")
        self.imageDown = pygame.image.load("Beatbox Fire Bolt Down.png")
