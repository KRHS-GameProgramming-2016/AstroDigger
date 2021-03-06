import pygame, sys, math, random
from Enemy import *

class Shade(Enemy):
    def __init__(self, speed=0, pos=[0,0], size=64):
        self.size = size
        self.imageLeft = pygame.image.load("Resources/Enemy/Enemy-shade-left.png")
        self.imageRight = pygame.image.load("Resources/Enemy/Enemy-shade-right.png")
        self.imageUp = pygame.image.load("Resources/Enemy/Enemy-shade-up.png")
        self.imageDown = pygame.image.load("Resources/Enemy/Enemy-shade-down.png")

        self.image = self.imageRight
        self.rect = self.image.get_rect(center = pos)
        self.maxSpeed = speed

        self.kind = "boss"

        self.decideDirection()


        self.didBounceX = False
        self.didBounceY = False
        self.hit = False
        self.inflationTime = 0
        self.inflationLevel = 0
        self.inflationMaxLevel = 19
        self.inflationMaxTime = 1

        self.state = "right"
        self.prevState = "right"
        
    def animate(self):
    #if self.prevState != self.state:
        self.prevState = self.state
        if self.state == "right":
            self.image = self.imageRight
        elif self.state == "left":
            self.image = self.imageLeft
        elif self.state == "up":
            self.image = self.imageUp
        elif self.state == "down":
            self.image = self.imageDown
        #self.frame = 0
        #self.maxFrame = len(self.images) - 1
        #self.animationTimer = self.animationTimerMax
