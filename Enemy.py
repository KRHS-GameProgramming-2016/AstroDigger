import pygame, sys, math

class Enemy():
    def __init__(self, image, speed=[0,0], pos=[0,0], size=64):
        self.image = pygame.image.load("Resources/Enemy/" + image)
        if size:
            self.image = pygame.transform.scale(self.image, [size, size])
        self.rect = self.image.get_rect(center = pos)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.didBounceX = False
        self.didBounceY = False
        
    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def bounceDirt(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if not self.didBounceX:
                    self.speedx = -self.speedx
                if not self.didBounceY:
                    self.speedy = -self.speedy
                    
    def dist(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        xDiff = x1 - x2
        yDiff = y1 - y2
        return math.sqrt(xDiff**2 + yDiff**2)
