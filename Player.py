import pygame, sys, math, time

class Player():
    
    def __init__(self,  size=[52, 56], maxSpeed =5 , speed=[0, 0], pos=[0,0]):
        self.imageLeft = pygame.image.load("Resources/Player/Player Left.png")
        self.imageRight = pygame.image.load("Resources/Player/Player Right.png")
        self.imageUpleft = pygame.image.load("Resources/Player/Player Upleft.png")
        self.imageUpright = pygame.image.load("Resources/Player/Player Upright.png")
        self.imageDownleft = pygame.image.load("Resources/Player/Player Downleft.png")
        self.imageDownright = pygame.image.load("Resources/Player/Player Downright.png")
        self.blankImage = pygame.image.load("Resources/Player/blank.png")
        self.digImage = pygame.image.load("Resources/digZone.png")
        self.inflateImageY = pygame.image.load("Resources/Enemy/ShootZoneY.png")
        self.inflateImageX = pygame.image.load("Resources/Enemy/ShootZoneX.png")
        self.inflateImage = self.inflateImageX
        self.size = size
        
        #self.inflateImage = self.inflateImageFalse
        
        self.horizontalsize = [self.size[0], self.size[1]]
        self.verticalsize = [self.size[1], self.size[0]]

        self.verticalsize = [size[0]-maxSpeed+(1/100), size[1]-maxSpeed+(1/100)]
        self.horizontalsize = [size[1]-maxSpeed+(1/100), size[0]-maxSpeed+(1/100)]      
        self.size = self.horizontalsize
        
        #self.size = [56,56]
        #self.imageLeft = pygame.transform.scale(self.imageLeft, self.size)
        #self.imageRight = pygame.transform.scale(self.imageRight, self.size)
        self.digImage = pygame.transform.scale(self.digImage, self.size)
        
        self.state = "right"
        self.prevState = "right"
        self.imageState = "right"
        self.image = self.imageRight
        self.rect = self.image.get_rect()
        
        
        self.digZone = self.digImage.get_rect()
        self.digZone.topleft = self.rect.topright
       
        self.inflateZone = self.inflateImage.get_rect()
        self.inflateZone.topleft = self.rect.topright
        
        self.inflating = False
        self.inflateHit = False
        self.inflateTimeractive = False
        self.digging = False
        self.hit = False
        
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
        self.blinkFrame = 0
      
    def animate(self):
        if self.prevState != self.state:
            if self.state == "right":
                self.size = self.horizontalsize
                self.image = self.imageRight
            elif self.state == "left":
                self.image = self.imageLeft
                self.size = self.horizontalsize
            elif self.state == "up":
                self.size = self.verticalsize
                if self.rect.right < 384:
                    self.image = self.imageUpright
                if self.rect.left > 384:
                    self.image = self.imageUpleft
            elif self.state == "down":
                self.size = self.verticalsize
                if self.rect.right < 384:
                    self.image = self.imageDownleft
                if self.rect.left > 384:
                    self.image = self.imageDownright

    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.digZone = self.digZone.move(self.speed)
        self.inflateZone = self.inflateZone.move(self.speed)
        self.digging = False
        self.animate()
        
    def direction(direction):
        return direction    
        
    def go(self, direction):
        if direction == "up":
            self.speedy = -self.maxSpeed
            self.digZone.left = self.rect.left
            self.digZone.bottom = self.rect.top
            self.inflateImage = self.inflateImageY
            self.inflateZone = self.inflateImage.get_rect()
            self.inflateZone.left = self.rect.left
            self.inflateZone.bottom = self.rect.top
            self.state = "up"
        if direction == "down":
            self.speedy = self.maxSpeed
            self.digZone.left = self.rect.left
            self.digZone.top = self.rect.bottom
            self.inflateImage = self.inflateImageY
            self.inflateZone = self.inflateImage.get_rect()
            self.inflateZone.left = self.rect.left
            self.inflateZone.top = self.rect.bottom
            self.state = "down"
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.digZone.top = self.rect.top
            self.digZone.right = self.rect.left
            self.inflateImage = self.inflateImageX
            self.inflateZone = self.inflateImage.get_rect()
            self.inflateZone.top = self.rect.top
            self.inflateZone.right = self.rect.left
            self.state = "left"
        if direction == "right":
            self.speedx = self.maxSpeed
            self.digZone.top = self.rect.top
            self.digZone.left = self.rect.right
            self.inflateZone.top = self.rect.top
            self.inflateZone.left = self.rect.right
            self.inflateImage = self.inflateImageX
            self.inflateZone = self.inflateImage.get_rect()
            self.inflateZone.top = self.rect.top
            self.inflateZone.left = self.rect.right
            self.state = "right"
            
        if direction == "stop up":
            self.speedy = 0
            self.prevState = "up"
        if direction == "stop down":
            self.speedy = 0
            self.prevState = "down"
        if direction == "stop left":
            self.speedx = 0
            self.prevState = "left"
        if direction == "stop right":
            self.speedx = 0
            self.prevState = "right"
        
    def dirtCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if not self.didBounceX:
                        self.speedx = -self.speedx
                        self.didBounceX = True
                    if not self.didBounceY:
                        self.speedy = -self.speedy
                        self.didBounceX = True
                    self.move()
                    self.speedx = 0
                    self.speedy = 0
                    
    def enemyCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if not self.didBounceX:
                        self.speedx = -self.speedx
                        self.didBounceX = True
                    if not self.didBounceY:
                        self.speedy = -self.speedy
                        self.didBounceX = True
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
        
    def inflate(self):
        self.inflating = True
        #self.inflateImage = self.inflateImagetrue
        
    def inflateTimer(self):
        if self.inflateTimeractive == False:
            self.startTime = time.clock()
            self.inflateTimeractive == True
        
        
    def blinkImage(self):
        if self.blinkFrame == 0:
            self.lives -= 1
            self.prevImage = self.image
            self.blinkFrame = 1
            
        self.blinkFrame1 = self.prevImage
        self.blinkFrame2 = self.blankImage
        
        if self.blinkFrame > 0:
            if self.blinkFrame % 2 == 0:
                self.image = self.blinkFrame2
            if self.blinkFrame % 2 != 0:
                self.image = self.blinkFrame1
            self.blinkFrame += 1
        
    def hitUpdate(self):
        self.hitFrame = 1
    
    def dig(self):
        self.digging = True
        
    def digCollide(self, dirt):
        if self.digging == True:
            if self.digZone.bottom > dirt.rect.top and self.digZone.top < dirt.rect.bottom: #top and bottom bounds
                if dirt.rect.left < self.digZone.right and dirt.rect.right > self.digZone.left: #left and right bounds
                    if self.state == "up" or self.state == "down": #up or down dig
                        if self.digZone.right - dirt.rect.left > self.size[0] / 2: 
                            if dirt.rect.right - self.digZone.left > self.size[0] / 2:
                                dirt.isDug = True
                    elif self.state == "left" or self.state == "right": #left or right dig
                        if self.digZone.bottom - dirt.rect.top > self.size[1] / 2: #if the distance between the digZone bottom and the dirt top is less than half the size
                            if dirt.rect.bottom - self.digZone.top > self.size[1] / 2:
                                dirt.isDug = True
    def inflateCollide(self, enemy):
        if self.inflating == True:
            if self.inflateZone.bottom > enemy.rect.top and self.inflateZone.top < enemy.rect.bottom: #top and bottom bounds
                if enemy.rect.left < self.inflateZone.right and enemy.rect.right > self.inflateZone.left: #left and right bounds
                    if self.state == "up" or self.state == "down": #up or down dig
                        if self.inflateZone.right - enemy.rect.left > self.size[0] / 2: 
                            if enemy.rect.right - self.inflateZone.left > self.size[0] / 2:
                                self.inflateHit = True
                                self.inflating = False
                    elif self.state == "left" or self.state == "right": #left or right dig
                        if self.inflateZone.bottom - enemy.rect.top > self.size[1] / 2: #if the distance between the inflateZone bottom and the enemy top is less than half the size
                            if enemy.rect.bottom - self.inflateZone.top > self.size[1] / 2:
                                self.inflateHit = True
                                self.inflating = False

