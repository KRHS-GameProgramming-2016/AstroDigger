import pygame, math, sys
from ShootingEnemy import *

class Bfire():
    def __init__(self, state, pos=[0,0], size=64):
        self.maxSpeed = 6
        self.size = size
        if state == "left":
            self.image = pygame.image.load("Resources/Enemy/Beatbox Fire Bolt Left.png")
            self.speed = [-self.maxSpeed, 0]
        elif state == "right":
            self.image = pygame.image.load("Resources/Enemy/Beatbox Fire Bolt Right.png")
            self.speed = [self.maxSpeed, 0]
        elif state == "up":
            self.image = pygame.image.load("Resources/Enemy/Beatbox Fire Bolt Up.png")
            self.speed = [0, -self.maxSpeed]
        else:
            self.image = pygame.image.load("Resources/Enemy/Beatbox Fire Bolt Down.png")
            self.speed = [0, self.maxSpeed]

        self.image = pygame.transform.scale(self.image, [self.size,self.size])
        self.rect = self.image.get_rect(center = pos)

        
        self.size = size
        self.pos = pos
        self.ded = False

    def move(self):
        self.rect = self.rect.move(self.speed)
    
    def dirtCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.ded = True
                
    def screenCollide(self, screenSize):
        screenWidth = screenSize[0]
        screenHeight = screenSize[1]
        if self.rect.top < 0 or self.rect.bottom > screenHeight:
            if self.rect.center[0] > screenWidth:
                self.ded = True
                
    def playerCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    other.hit = True
                    self.ded = True
                    
    def enemyCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    other.hit = True
                    self.ded = True

