import pygame, sys, math

class Player():
    
    def __init__(self, maxSpeed =5 , pos=[0,0], size=[64,64]):
        self.image = pygame.image.load("Resources/Enemy/Enemy-Pew.png")
        self.rect = self.image.get_rect()
        self.speed = [1, 1]
        self.maxSpeed = maxSpeed     
        self.images = [
                      ]
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.animationTimer = 0
        self.animationTimerMax = .2 * 60 #seconds * 60 fps
    
    def move(self):
        self.rect = self.rect.move(self.speed)
        self.animate()
    
    def dirtCollide(self, dirt):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                return True
        return False
    
    def screenCollide(self, screenSize):
        if pos[0] == screenSize[0]:
            pos[0] = 0
        
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
        
    def inflate(self, enemy):
        #need the timer
        enemy.speed = [0, 0]
        if enemy.inflationLevel < 3:
            enemy.image = pygame.image.load("Resources/Enemy/Inflation/" +str(enemy.inflationLevel) +".png")
            enemy.inflationLevel += 1
        else: 
            enemies.remove(enemy)
        
        
        
    def dig(self, dirt):
        pass
        
    def collideEnemy(self, enemy):
         if self.rect.right > enemy.rect.left and self.rect.left < enemy.rect.right:
            if self.rect.bottom > enemy.rect.top and self.rect.top < enemy.rect.bottom:
                pass
