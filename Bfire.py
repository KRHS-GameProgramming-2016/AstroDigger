import pygame, math, sys

class Bfire():
    def __init__(self, speed=0, pos=[0,0], size=64):
        self.imageLeft = pygame.image.load("Resources/Enemy/Beatbox Fire Bolt Left.png")
        self.imageRight = pygame.image.load("Resources/Enemy/Beatbox Fire Bolt Right.png")
        self.imageUp = pygame.image.load("Resources/Enemy/Beatbox Fire Bolt Up.png")
        self.imageDown = pygame.image.load("Resources/Enemy/Beatbox Fire Bolt Down.png")

        self.imageLeft = pygame.transform.scale(self.imageLeft, [self.size,self.size])
        self.imageRight = pygame.transform.scale(self.imageRight, [self.size,self.size])
        self.imageUp = pygame.transform.scale(self.imageUp, [self.size,self.size])
        self.imageDown = pygame.transform.scale(self.imageDown, [self.size,self.size])
        self.rect = self.image.get_rect(center = pos)
        self.image = self.imageRight

        self.speed = speed
        self.size = size
        self.pos = pos

    def move(speed):
        pass
