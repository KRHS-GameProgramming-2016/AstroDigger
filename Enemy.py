import pygame, sys, math, random

class Enemy():
    def __init__(self, speed=0, pos=[0,0], size=64):
        self.size = size
        self.imagesLeft = [pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Pew Left.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Pew Left2.png"), [self.size,self.size])]
        self.imagesRight = [pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Pew Right.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Pew Right2.png"), [self.size,self.size])]
        self.imagesUp = [pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Pew Up.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Pew Up2.png"), [self.size,self.size])]
        self.imagesDown = [pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Pew Down.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Pew Down2.png"), [self.size,self.size])]
        self.blankImage = pygame.image.load("Resources/Player/blank.png")


        self.maxSpeed = speed

        self.kind = "normal"

        self.didBounceX = False
        self.didBounceY = False
        self.inflationTime = 0
        self.inflationLevel = 0
        self.inflationMaxLevel = 10
        self.inflationMaxTime = 2

        self.state = "right"
        self.prevState = "right"

        self.frame = 0
        self.blinkFrame = 0

        self.animationTimer = 0
        self.animationTimerMax = .3 * 60 #seconds * 60 fps

        self.images = self.imagesRight
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.maxFrame = len(self.images) - 1
        
        self.decideDirection()
        
        self.hit = False


    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        if self.speedx != 0:     #moving left/right
            if self.rect.left % self.size == 0:
                self.decideDirection()
        else:     #moving up/down
            if self.rect.top % self.size == 0:
                self.decideDirection()
        self.animate()

    def decideDirection(self):
        d = random.randint(0,3)
        if d == 0:
            self.speedx = 0
            self.speedy = -self.maxSpeed
            self.state = "up"
        elif d == 1:
            self.speedx = self.maxSpeed
            self.speedy = 0
            self.state = "right"
        elif d == 2:
            self.speedx = 0
            self.speedy = self.maxSpeed
            self.state = "down"
        elif d == 3:
            self.speedx = -self.maxSpeed
            self.speedy = 0
            self.state = "left"

    def animate(self):
        if self.prevState != self.state:
            self.prevState = self.state
            if self.state == "right":
                self.images = self.imagesRight
            elif self.state == "left":
                self.images = self.imagesLeft
            elif self.state == "up":
                self.images = self.imagesUp
            elif self.state == "down":
                self.images = self.imagesDown
            self.frame = 0
            self.maxFrame = len(self.images) - 1
            self.animationTimer = self.animationTimerMax

        if self.animationTimer < self.animationTimerMax:
            self.animationTimer += 1
        else:
            self.animationTimer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.images[self.frame]
            
            
    def blinkImage(self):
        if self.blinkFrame == 0:
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

    def dirtCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.speedx = -self.speedx
                self.speedy = -self.speedy
                self.didBounceX = True
                self.didBounceY = True
                self.move()

    def screenCollide(self, screenSize):
        screenWidth = screenSize[0]
        screenHeight = screenSize[1]
        if self.rect.top < 0 or self.rect.bottom > screenHeight:
            self.speedy = -self.speedy
        if self.rect.center[0] > screenWidth:
            self.rect.center = [0, self.rect.center[1]]
        elif self.rect.center[0] < 0:
            self.rect.center = [screenWidth, self.rect.center[1]]

    def playerCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    self.speedx = -self.speedx
                    self.speedy = -self.speedy
                    self.move()
                    other.hit = True

    #def playerCollide(self, other):
        #if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                #if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    #diffX = self.rect.centerx - other.rect.centerx
                    #diffY = self.rect.centery - other.rect.centery
                    #if abs(diffX) > abs(diffY): #left right collide
                        #if diffX > 0: #left
                            #self.rect.left = other.rect.right + 1
                        #else:
                            #self.rect.right = other.rect.left - 1
                        #self.speedx = 0
                        #other.hit = True
                    #else:
                        #if diffY > 0: #below
                            #self.rect.top = other.rect.bottom + 1
                        #else:
                            #self.rect.bottom = other.rect.top - 1
                        #self.speedy = 0
                        #other.hit = True


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
