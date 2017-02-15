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
        self.inflationTime = 0
        self.inflationLevel = 0
        self.inflationMax = 10

        self.state = "right"
        self.prevState = "right"
