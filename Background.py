import math, sys, pygame

class Background():
    def __init__(self, size=None):
        self.image = pygame.image.load("Resources/Backgrounds/killmenow.jpg")
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        
if __name__ == "__main__":
    pygame.init()

    clock = pygame.time.Clock()

    width = 768
    height = 640
    size = width, height
    screen = pygame.display.set_mode(size)
 
