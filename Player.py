import pygame, sys, math

class Player():
    
    def __init__(self,  size=[64,64], maxSpeed =5 , speed=[0, 0], pos=[0,0]):
        self.imageLeft = pygame.image.load("Resources/Player/Player Left.png")
        self.imageRight = pygame.image.load("Resources/Player/Player Right.png")
        self.imageup = pygame.image.load("Resources/Player/Player Right.png")
        self.imageown = pygame.image.load("Resources/Player/Player Up.png")
        self.image = pygame.image.load("Resources/Player/Player Down.png")
        self.digImage = pygame.image.load("Resources/digZone.png")
        
        self.size = [size[0]-maxSpeed+1, size[1]-maxSpeed+1]
        self.size = [60,60]
        self.imageLeft = pygame.transform.scale(self.imageLeft, self.size)
        self.imageRight = pygame.transform.scale(self.imageRight, self.size)
        self.digImage = pygame.transform.scale(self.digImage, self.size)
        
        self.state = "right"
        self.prevState = "right"
        self.image = self.imageRight
        self.rect = self.image.get_rect()
        self.digZone = self.digImage.get_rect()
        self.digZone = self.digZone.move(size[0], 0)
        self.inflationLevel = 0
        self.digging = False
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.didBounceX = False
        self.didBounceY = False
        self.pos = [self.rect.left, self.rect.top]
        self.lives = 5
        self.maxSpeed = maxSpeed     
        self.images = [
                      ]
        
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
            elif self.state == "up":
                self.image = self.imageUp
            elif self.state == "down":
                self.image = self.imageDown

    
    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.digZone = self.digZone.move(self.speed)
        self.digging = False
        self.animate()
        
    def direction(direction):
        return direction    
        
    def go(self, direction):
        if direction == "up":
            self.speedy = -self.maxSpeed
            self.digZone.left = self.rect.left
            self.digZone.bottom = self.rect.top
            self.state = "up"
        if direction == "down":
            self.speedy = self.maxSpeed
            self.digZone.left = self.rect.left
            self.digZone.top = self.rect.bottom
            self.state = "down"
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.digZone.top = self.rect.top
            self.digZone.right = self.rect.left
            self.state = "left"
        if direction == "right":
            self.speedx = self.maxSpeed
            self.digZone.top = self.rect.top
            self.digZone.left = self.rect.right
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
                    self.didBounceX = True
                    self.speedy = 0
                    self.didBounceY = True
    
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
        for enemy in enemies:
            if self.digZone.left < enemy.rect.left:
                if self.digZone.right > enemy.rect.right:
                    if self.state == "UpRight" or "UpLeft":
                        if self.digZone.top < enemy.rect.bottom:
                            enemies.remove(enemy)
                    if self.state == "DownRight" or "DownLeft":
                        if self.digZone.bottom > enemy.rect.top:
                            enemy.speed = [0, 0]
                            if self.inflationLevel < 3:
                                #enemy.image = pygame.image.load("Resources/Enemy/Inflation/" +str(enemy.inflationLevel) +".png")
                                self.inflationLevel += 1
                            else: 
                                enemies.remove(enemy)
            if self.digZone.bottom > enemy.rect.bottom:
                if self.digZone.top < enemy.rect.top:
                    if self.state == "left":
                        if self.digZone.left < enemy.rect.right:
                            enemies.remove(enemy)
                    if self.state == "right":
                        if self.digZone.right > enemy.rect.left:
                            enemies.remove(enemy)

        
        
    def dig(self):
        self.digging = True
        
    def digCollide(self, dirt):
        if self.digging == True:
            if self.digZone.right > dirt.rect.left and self.digZone.left < dirt.rect.right:
                if self.digZone.bottom > dirt.rect.top and self.digZone.top < dirt.rect.bottom:
                        dirt.isDug = "dug"
        
    def enemyCollide(self, enemy):
         if self.rect.right > enemy.rect.left and self.rect.left < enemy.rect.right:
            if self.rect.bottom > enemy.rect.top and self.rect.top < enemy.rect.bottom:
                self.lives = self.lives - 1
