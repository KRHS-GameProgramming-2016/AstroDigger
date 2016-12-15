import pygame, sys, math

class Player():
    
    def __init__(self,  size=[64,64], maxSpeed =5 , speed=[0, 0], pos=[0,0]):
        self.imageLeft = pygame.image.load("Resources/Player/Player Left.png")
        self.imageRight = pygame.image.load("Resources/Player/Player Right.png")
        self.image = self.imageRight
        self.state = "right"
        self.prevState = "right"
        self.rect = self.image.get_rect()
        self.digImage = pygame.image.load("Resources/Player/blank.png")
        self.digImage = pygame.transform.scale(self.digImage, [128,128])
        self.digZone = self.rect.copy()
        self.digZone = self.digZone.inflate(self.rect.width, self.rect.height)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.pos = [self.rect.left, self.rect.top]
        self.lives = 5
        self.maxSpeed = maxSpeed     
        self.images = [
                      ]
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.animationTimer = 0
        self.animationTimerMax = .2 * 60 #seconds * 60 fps
    
    def animate(self):
        if self.prevState != self.state:
            self.prevState = self.state
            if self.state == "right":
                self.image = self.imageRight
            elif self.state == "left":
                self.image = self.imageLeft
            elif self.state == "Upleft":
                self.image = self.imageLeft
            elif self.state == "Downleft":
                self.image = self.imageLeft
            elif self.state == "UpRight":
                self.image = self.imageLeft
            elif self.state == "DownRight":
                self.image = self.imageLeft
                
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.digZone = self.digZone.move(self.speed)
        self.animate()
        
    def direction(direction):
        return direction    
        
    def go(self, direction):
        if direction == "up":
            self.speedy = -self.maxSpeed
            self.state = "up"
        if direction == "down":
            self.speedy = self.maxSpeed
            self.state = "down"
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.state = "left"
        if direction == "right":
            self.speedx = self.maxSpeed 
            self.state = "right"
            
        if direction == "stop up":
            self.speedy = 0
        if direction == "stop down":
            self.speedy = 0
        if direction == "stop left":
            if self.speedx < 0:
                self.speedx = 0
        if direction == "stop right":
            if self.speedx > 0:
                self.speedx = 0
        
    def dirtCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    self.speedx = -self.speedx
                    self.speedy = -self.speedy
                    self.move()
                    self.speedx = 0
                    self.speedy = 0
    
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
        
    def inflate(self, enemies):
        self.inflater.rect = self.rect
        if self.state == "up":
            self.inflater.rect.top = 0
        if self.state == "down":
            self.inflater.rect.bottom = 640
        if self.state == "left":
            self.inflater.rect.left = 0
        if self.state == "right":
            self.inflater.rect.right = 768
        for enemy in enemies:
            if self.inflater.rect.right > enemy.rect.left and self.inflater.rect.left < enemy.rect.right:
                if self.inflater.rect.bottom > enemy.rect.top and self.inflater.rect.top < enemy.rect.bottom:
                    enemy.speed = [0, 0]
                    if enemy.inflationLevel < 3:
                        enemy.image = pygame.image.load("Resources/Enemy/Inflation/" +str(enemy.inflationLevel) +".png")
                        enemy.inflationLevel += 1
                    else: 
                        enemies.remove(enemy)
        
        
        
    def dig(self, dirts):
        for dirt in dirts:
            if self.digZone.left < dirt.rect.left:
                if self.digZone.right > dirt.rect.right:
                    if self.state == "up":
                        if self.digZone.top < dirt.rect.bottom:
                            dirts.remove(dirt)
                    if self.state == "down":
                        if self.digZone.bottom > dirt.rect.top:
                            dirts.remove(dirt)
            if self.digZone.bottom > dirt.rect.bottom:
                if self.digZone.top < dirt.rect.top:
                    if self.state == "left":
                        if self.digZone.left > dirt.rect.right:
                            dirts.remove(dirt)
                    if self.state == "right":
                        if self.digZone.right > dirt.rect.left:
                            dirts.remove(dirt)
        
    def enemyCollide(self, enemy):
         if self.rect.right > enemy.rect.left and self.rect.left < enemy.rect.right:
            if self.rect.bottom > enemy.rect.top and self.rect.top < enemy.rect.bottom:
                self.lives = self.lives - 1
