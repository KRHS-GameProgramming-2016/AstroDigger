import math, sys, pygame

class Background():
    def __init__(self, size=None):
        self.image = pygame.image.load("Resources/Backgrounds/killmeagain.jpg")
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
