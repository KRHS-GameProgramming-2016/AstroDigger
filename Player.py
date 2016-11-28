import pygame, sys, math

class Player():
    
    def __init__(self, maxSpeed =5 , pos=[0,0], size=[64,64]):
        
        self.rect = self.image.get_rect(center = pos)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.maxSpeed = maxSpeed     
        self.images = [pygame.image.load("rsc/ball/playerball_up_1.png"),
                       pygame.image.load("rsc/ball/playerball_up_2.png")
                      ]
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.animationTimer = 0
        self.animationTimerMax = .2 * 60 #seconds * 60 fps
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
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
        #kskssksk
        
    def inflate(self):
        #inflatingnggn
        
    def dig(self, dirt):
        #sksksks
        
    def collideEnemy(self, enemy):
         if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                #the player dies
