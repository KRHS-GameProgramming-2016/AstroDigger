import pygame, math, sys
from Player import *

class Playerfire():
    def __init__(self, state, pos=[0,0], size=10):
        self.maxSpeed = 2
        self.size = size
        self.inflateHit = False
        if state == "right":
            self.image = pygame.image.load("Resources/Player/simple bullet.png")
            self.speed = [self.maxSpeed, 0]
            self.inflateHit = False
        if state == "left":
            self.image = pygame.image.load("Resources/Player/simple bullet.png")
            self.speed = [-self.maxSpeed, 0]
            self.inflateHit = False
        elif state == "up":
            self.image = pygame.image.load("Resources/Player/simple bullet vertical.png")
            self.speed = [0, -self.maxSpeed]
            self.inflateHit = False
        elif state == "down":
            self.image = pygame.image.load("Resources/Player/simple bullet vertical.png")
            self.speed = [0, self.maxSpeed]
            self.inflateHit = False

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
                    
    def enemyCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    other.hit = True
                    self.ded = True
                    self.inflateHit = True

