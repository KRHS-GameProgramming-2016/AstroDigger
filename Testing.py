import  pygame, sys, math
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
level = Level("Digger level1.lvl", 11)

enemies = level.enemies
print len(enemies)

player = Player()
dirts = level.dirts
timer = Timer([width/2, 50])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.go("up")
            if event.key == pygame.K_DOWN:
                player.go("down")
            if event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_LEFT:
                player.go("left")
            if event.key == pygame.K_d:
                player.dig()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_LEFT:
                player.go("stop left")
                
    player.screenCollide(width)
    for enemy in enemies:
        enemy.screenCollide(width)
    for dirt in dirts:
        player.dirtCollide(dirt)
        if player.digging:
            player.digDirt(dirt)
        for enemy in enemies:
            enemy.dirtCollide(dirt)
    
    timer.update()
        
    player.move() 
    for enemy in enemies:
        enemy.move()   
        
    bgColor = r,g,b = 0,0,0
    screen.fill(bgColor)
    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect)
    screen.blit(player.image, player.rect)
    for dirt in dirts:
        screen.blit(dirt.image, dirt.rect)
    screen.blit(timer.image, timer.rect)
    pygame.display.flip()
    clock.tick(60)