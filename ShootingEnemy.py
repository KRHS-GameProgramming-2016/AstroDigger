import pygame, sys, math, random, time
from Enemy import *
from Bfire import *
class ShootingEnemy(Enemy):
    def __init__(self, speed=0, pos=[0,0], size=64):
        self.shootXImage = pygame.image.load("Resources/Enemy/ShootZoneX.png")
        self.shootYImage = pygame.image.load("Resources/Enemy/ShootZoneY.png")
        self.speed = [speed, 0]
        Enemy.__init__(self, speed, pos, size)
        self.imagesLeft = [pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Beatbox Left.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Beatbox Left2.png"), [self.size,self.size])]
        self.imagesRight = [pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Beatbox Right.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Beatbox Right2.png"), [self.size,self.size])]
        self.imagesUp = [pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Beatbox Up.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Beatbox Up2.png"), [self.size,self.size])]
        self.imagesDown = [pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Beatbox Down.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Resources/Enemy/Enemy-Beatbox Down2.png"), [self.size,self.size])]

    

        self.pos = pos

        self.kind = "shooting"
        self.notStopped = True

        self.didBounceX = False
        self.didBounceY = False
        self.inflationTime = 0
        self.inflationLevel = 0
        self.inflationMaxLevel = 5
        self.inflationMaxTime = 2

        self.state = "right"
        self.prevState = "right"

        self.frame = 0

        self.animationTimer = 0
        self.animationTimerMax = .3 * 60 #seconds * 60 fps

        self.images = self.imagesRight
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.maxFrame = len(self.images) - 1
        
        self.decideDirection()
        
        self.shootTimerMax = 3*60
        self.shootTimer = self.shootTimerMax
        self.inflationMaxLevel = 10
        self.inflationMaxTime = 1

    def decideDirection(self):
        d = random.randint(0,3)
        if self.speed != [0,0]:
            if d == 0: #up
                self.speedx = 0
                self.speedy = -self.maxSpeed
                self.state = "up"
                self.shootImage = self.shootYImage
                self.shootZone = self.shootImage.get_rect(midbottom = self.rect.midtop)
            elif d == 1: #right
                self.speedx = self.maxSpeed
                self.speedy = 0
                self.state = "right"
                self.shootImage = self.shootXImage
                self.shootZone = self.shootImage.get_rect(midleft = self.rect.midright)
            elif d == 2: #down
                self.speedx = 0
                self.speedy = self.maxSpeed
                self.state = "down"
                self.shootImage = self.shootYImage
                self.shootZone = self.shootImage.get_rect(midtop = self.rect.midbottom)
            elif d == 3: #left
                self.speedx = -self.maxSpeed
                self.speedy = 0
                self.state = "left"
                self.shootImage = self.shootXImage
                self.shootZone = self.shootImage.get_rect(midright = self.rect.midleft)

    def shoot(self, player):
        if self.shootZone.right > player.rect.left and self.shootZone.left < player.rect.right:
            if self.shootZone.bottom > player.rect.top and self.shootZone.top < player.rect.bottom:
                self.notStopped = False
                if self.shootTimer < self.shootTimerMax:
                    self.shootTimer += 1
                    return False
                else:
                    self.shootTimer = 0
                    return True
        self.notStopped = True
        if self.shootTimer < self.shootTimerMax:
            self.shootTimer += 1
        return False
        

    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        if self.notStopped:
            self.speed = [self.speedx, self.speedy]
            self.rect = self.rect.move(self.speed)
            self.shootZone = self.shootZone.move(self.speed)

            if self.speedx != 0:     #moving left/right
                if self.rect.left % self.size == 0:
                    #print "left/right", self.rect.center[0]
                    self.decideDirection()
            else:     #moving up/down
                if self.rect.top % self.size == 0:
                    #print "left/right", self.rect.center[1]
                    self.decideDirection()
        self.animate()

#if __name__ == "__main__":
    #pygame.init()

    #clock = pygame.time.Clock()

    #width = 768
    #height = 640
    #size = width, height
    #screen = pygame.display.set_mode(size)

    #e = ShootingEnemy(0, [200,200])
    #down = False
    #while True:
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT: sys.exit()
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #down = True
            #if event.type == pygame.MOUSEBUTTONUP:
                #down = False

            #if down:
                #bgColor = 0,0,0

                #screen.fill(bgColor)
                #screen.blit(e.imageSLeft, e.rect)
            #else:
                #bgColor = 0,0,0

                #screen.fill(bgColor)
                #screen.blit(e.imageLeft, e.rect)

            #pygame.display.flip()
            #clock.tick(60)
