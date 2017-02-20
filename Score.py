import pygame, sys, math

class Score():                                      #Edit these two
    def __init__(self, pos):#                                   |        
        self.value = 0                #                         |----------|          
        #http://www.1001fonts.com/bustin-jieber-font.html      \|/        \|/
        self.font = pygame.font.Font("Resources/Fonts/united-kingdom/United Kingdom DEMO.otf", 40)
        self.image = self.font.render("Score: " + str(self.value), True, (255,0,0))
        self.rect = self.image.get_rect(center = pos)

#Types of fonts
#united-kingdom/United Kingdom DEMO.otf
#power-pixel-7/power_pixel-7.ttf
#Bustin Jieber/Bustin Jieber.otf

    def change(self, amount = 1):
        self.value += amount
        if self.value <= 0:
            self.value = 0
        self.image = self.font.render("Score: " + str(self.value), True, (255,0,0))
        self.rect = self.image.get_rect(center = self.rect.center)
