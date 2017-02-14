import math, sys, pygame

class Background():
    def __init__(self, size=None):
        self.image = pygame.image.load("Resources/Backgrounds/noplz.jpg")
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
#Types of Backgrounds you can choose
#why.jpg
#killmenow.jpg
#killmeagain.jpg
#killme.jpg
#noplz.jpg
