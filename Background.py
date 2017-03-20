import math, sys, pygame, random
from LevelNumber import *

class Background():
    def __init__(self, size=None):
        self.image = self.decideBackground()
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()

    def decideBackground(self):
        images = ["Resources/Backgrounds/emailtojoe.jpg",
                  "Resources/Backgrounds/asteroid.jpg",
                  "Resources/Backgrounds/spoopy.jpg",
                  "Resources/Backgrounds/space.jpg",
                  "Resources/Backgrounds/asteroids.jpg",
                  "Resources/Backgrounds/moreasteroids.jpg",
                  "Resources/Backgrounds/generic.jpg"]
        b = random.randint(0, len(images)-1)
        return pygame.image.load(images[b])
