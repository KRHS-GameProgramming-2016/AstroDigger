import math, sys, pygame, random

class Background():
    def __init__(self, size=None):
        self.image = self.decideBackground()
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()

    def decideBackground(self):
        images = ["Resources/Backgrounds/why.jpg",
                  "Resources/Backgrounds/killmenow.jpg",
                  "Resources/Backgrounds/killmeagain.jpg",
                  "Resources/Backgrounds/killme.jpg",
                  "Resources/Backgrounds/noplz.jpg",
                  "Resources/Backgrounds/lel2.jpg",
                  "Resources/Backgrounds/art.jpg",
                  "Resources/Backgrounds/cool-and-good.jpg",
                  "Resources/Backgrounds/ANGERY.jpg"]
        b = random.randint(0, len(images)-1)
        return pygame.image.load(images[b])
        





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
