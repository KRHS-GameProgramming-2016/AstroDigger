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

level = Level("diggerlevel1.lvl")

enemies = [Enemy("enemy")]

player = Player
walls = level.walls

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if using == "keyboard":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.go("up")
                if event.key == pygame.K_DOWN:
                    player.go("down")
                if event.key == pygame.K_RIGHT:
                    player.go("right")
                if event.key == pygame.K_LEFT:
                    player.go("left")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_LEFT:
                    player.go("stop left")
        else:
            if event.type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(False)
                player.goMouse(event.pos)
                
    player.move()
    player.bounceScreen(size)
    for wall in walls:
        player.bounceWall(wall)
        
    bgColor = r,g,b
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    clock.tick(60)

