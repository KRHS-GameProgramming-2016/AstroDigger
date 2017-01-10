import pygame, sys, math, random

class Enemy():
    def __init__(self, speed=0, pos=[0,0], size=64):
        self.size = size
        self.imageLeft = pygame.image.load("Resources/Enemy/Enemy-Pew Left.png"
                                           "Resources/Enemy/Enemy-Pew Left2.png")
        self.imageRight = pygame.image.load("Resources/Enemy/Enemy-Pew Right.png"
                                            "Resources/Enemy/Enemy-Pew Right2.png")
        self.imageUp = pygame.image.load("Resources/Enemy/Enemy-Pew Up.png"
                                         "Resources/Enemy/Enemy-Pew Up2.png")
        self.imageDown = pygame.image.load("Resources/Enemy/Enemy-Pew Down.png")
                                           "Resources/Enemy/Enemy-Pew Down2.png")
        
        self.imageLeft = pygame.transform.scale(self.imageLeft, [self.size,self.size])
        self.imageRight = pygame.transform.scale(self.imageRight, [self.size,self.size])
        self.imageUp = pygame.transform.scale(self.imageUp, [self.size,self.size])
        self.imageDown = pygame.transform.scale(self.imageDown, [self.size,self.size])
        self.image = self.imageRight
        self.rect = self.image.get_rect(center = pos)
        self.maxSpeed = speed
        
        self.kind = "normal"
        
        self.decideDirection()

        
        self.didBounceX = False
        self.didBounceY = False
        self.inflation = 0
        
        self.state = "right"
        self.prevState = "right"
        
        
    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        if self.speedx != 0:     #moving left/right
            if self.rect.left % self.size == 0:
                #print "left/right", self.rect.center[0]
                self.decideDirection()
        else:     #moving up/down
            if self.rect.top % self.size == 0:
                #print "left/right", self.rect.center[1]
                self.decideDirection()
        self.animate()
     
    def decideDirection(self):
        d = random.randint(0,3)
        if d == 0: #up
            self.speedx = 0
            self.speedy = -self.maxSpeed
            self.state = "up"
        elif d == 1: #right
            self.speedx = self.maxSpeed
            self.speedy = 0
            self.state = "right"
        elif d == 2: #down
            self.speedx = 0
            self.speedy = self.maxSpeed
            self.state = "down"
        elif d == 3: #left
            self.speedx = -self.maxSpeed
            self.speedy = 0
            self.state = "left"
            
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
            #print self.state
            
        
    def dirtCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if not self.didBounceX:
                    self.speedx = -self.speedx
                if not self.didBounceY:
                    self.speedy = -self.speedy
                    
    def screenCollide(self, screenSize):
        screenWidth = screenSize[0]
        screenHeight = screenSize[1]
        if self.rect.top < 0 or self.rect.bottom > screenHeight:
            self.speedy = -self.speedy
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

#if __name__ == "__main__":
    #pygame.init()

    #clock = pygame.time.Clock()

    #width = 768
    #height = 640
    #size = width, height
    #screen = pygame.display.set_mode(size)

    #e = Enemy(0, [200,200])
    #down = False
    #while True:
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT: sys.exit()
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #down = True
            #if event.type == pygame.MOUSEBUTTONUP:
                #down = False
                
            #if down:
                #bgColor = 0,0,255
               
                #screen.fill(bgColor)
                #screen.blit(e.imageSLeft, e.rect)
            #else:
                #bgColor = 255,0,0
               
                #screen.fill(bgColor)
                #screen.blit(e.imageLeft, e.rect)
                
            #pygame.display.flip()
            #clock.tick(60)
