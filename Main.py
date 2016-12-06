import pygame, sys, math
from Player import *
from Enemy import *
from Dirt import *
from Timer import *
from Score import *
from Level import *
pygame.init()

clock = pygame.time.Clock()

width = 768
height = 640
size = width, height
screen = pygame.display.set_mode(size)

bgColor = 0,0,0

level = Level("Digger level1.lvl")

enemies = [Enemy("Enemy-Pew.png")]

player = Player()
walls = level.walls

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move("up")
            if event.key == pygame.K_DOWN:
                player.move("down")
            if event.key == pygame.K_RIGHT:
                player.move("right")
            if event.key == pygame.K_LEFT:
                player.move("left")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.move("stop up")
            if event.key == pygame.K_DOWN:
                player.move("stop down")
            if event.key == pygame.K_RIGHT:
                player.move("stop right")
            if event.key == pygame.K_LEFT:
                player.move("stop left")
                
    player.screenCollide(width)
    for wall in walls:
        player.bounceWall(wall)
        
        
    bgColor = r,g,b = 0,0,0
    screen.fill(bgColor)
    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect)
    screen.blit(player.image, player.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    clock.tick(60)
