import math, sys, pygame, random
                                                             
class Background():                                          
    def __init__(self, size=None):                           
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()

    def decideBackground
        b = random.randint(0,8)
        if b == 0:
            self.image = pygame.image.load("Resources/Backgrounds/why.jpg")





#Types of Backgrounds
#why.jpg
#killmenow.jpg
#killmeagain.jpg
#killme.jpg
#noplz.jpg
#lel2.jpg
#art.jpg
#cool-and-good.jpg
#ANGERY.jpg
