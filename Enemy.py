import pygame, sys, math, random

class Enemy():
    def __init__(self, image, speed=[0,0], pos=[0,0], size=64):
        self.image = pygame.image.load("Resources/Enemy/" + image)
        if size:
            self.image = pygame.transform.scale(self.image, [size, size])
        self.rect = self.image.get_rect(center = pos)
        self.maxSpeed = speed
        self.decideDirection()
        self.didBounceX = False
        self.didBounceY = False
        self.size = size
        
        
    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        if self.speedx != 0:     #moving left/right
            if self.rect.left % self.size == 0:
                print "left/right", self.rect.center[0]
                self.decideDirection()
        else:     #moving up/down
            if self.rect.top % self.size == 0:
                print "left/right", self.rect.center[1]
                self.decideDirection()
     
    def decideDirection(self):
        d = random.randint(0,3)
        if d == 0: #up
            self.speedx = 0
            self.speedy = -self.maxSpeed
        elif d == 1: #right
            self.speedx = self.maxSpeed
            self.speedy = 0
        elif d == 2: #down
            self.speedx = 0
            self.speedy = self.maxSpeed
        elif d == 3: #left
            self.speedx = -self.maxSpeed
            self.speedy = 0
            
        
    def dirtCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if not self.didBounceX:
                    self.speedx = -self.speedx
                if not self.didBounceY:
                    self.speedy = -self.speedy
                    
    def screenCollide(self, screenWidth):
        if self.rect.center[0] > screenWidth:
            self.rect.center = [0, self.rect.center[1]]
        elif self.rect.center[0] < 0:
            self.rect.center = [screenWidth, self.rect.center[1]]
                    
    def dist(self, pt):
        x = pt[0] - self.rect.right
        y = pt[1] - self.rect.bottom
        if x < 0:
            x += -64
            x += x
        if y < 0:
            y += -64
            y += y
        return [x, y]
        return math.sqrt(xDiff**2 + yDiff**2)
