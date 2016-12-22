import pygame, sys, math, random
from Enemy import *
class ShootingEnemy(Enemy):
    def __init__(self, speed=[0,0], pos=[0,0], size=64):
        Enemy.__init__(self, speed, pos, size)
        self.imageLeft = pygame.image.load("Resources/Enemy/Enemy-Beatbox Left.png")
        self.imageRight = pygame.image.load("Resources/Enemy/Enemy-Beatbox Right.png")
        self.imageUp = pygame.image.load("Resources/Enemy/Enemy-Beatbox Up.png")
        self.imageDown = pygame.image.load("Resources/Enemy/Enemy-Beatbox Down.png")
        self.ShootImage = pygame.image.load("Resources/Enemy/ShootZone.png")
        
        self.imageLeft = pygame.transform.scale(self.imageLeft, [self.size,self.size])
        self.imageRight = pygame.transform.scale(self.imageRight, [self.size,self.size])
        self.imageUp = pygame.transform.scale(self.imageUp, [self.size,self.size])
        self.imageDown = pygame.transform.scale(self.imageDown, [self.size,self.size])
        self.image = self.imageRight
        self.rect = self.image.get_rect(center = pos)
        
        
