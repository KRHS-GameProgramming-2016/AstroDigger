import  pygame, sys, math
from Player import *
from Enemy import *
from ShootingEnemy import *
from Shade import *
from Dirt import *
from Timer import *
from Score import *
from Level import *
from Background import *
from Lives import *
from LevelNumber import *
pygame.init()

clock = pygame.time.Clock()

width = 768
height = 640
size = width, height
screen = pygame.display.set_mode(size)

bgColor = 0,0,0
level = Level("Digger level1.lvl", 1)
levelNumber = 1
BG = Background(size)

enemies = level.enemies
print len(enemies)

player = Player()
dirts = level.dirts
playerLives = player.lives
timer = Timer([width*.75, 50])
lives = Lives([width*.25, 50])
levelnumberShow = LevelNumber([width*.25, 100])
bullets = []
playerBullets = []
while player.lives > 0:
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
            if event.key == pygame.K_SPACE:
                player.inflate()
            #for testing purposes DELETE LATER
            if event.key == pygame.K_w:
                levelNumber += 1
                level = Level("Digger level1.lvl", levelNumber)
                enemies = level.enemies
                player = Player()
                dirts = level.dirts
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_LEFT:
                player.go("stop left")

    player.screenCollide(size)
    for enemy in enemies:
        enemy.screenCollide(size)
        player.enemyCollide(enemy)
        enemy.playerCollide(player)
        player.inflateCollide(enemy)
        if enemy.kind == "shooting":
            if enemy.shoot(player):
                bullets += [Bfire(enemy.state, enemy.rect.center)]
        if player.inflateHit == True:
            enemy.speedx = 0
            enemy.speedy = 0
            enemy.inflationLevel += 1
            enemy.inflationTime = timer.value
            player.inflateHit = False
        if enemy.inflationTime > 0:
            if (timer.value - enemy.inflationTime) > enemy.inflationMaxTime:
                enemy.speedx = enemy.maxSpeed
                enemy.speedy = enemy.maxSpeed
                enemy.inflationTime = 0
                enemy.inflationLevel = 0
                print enemy.inflationTime
        if enemy.inflationLevel > enemy.inflationMaxLevel:
            enemies.remove(enemy)
    
    if len(enemies) == 0:
        levelNumber += 1
        level = Level("Digger level1.lvl", levelNumber)
        enemies = level.enemies
        player = Player()
        dirts = level.dirts
        player.lives = 5
        playerLives = player.lives
        BG = Background(size)
        

            
    for bullet in bullets:
        bullet.move()
    
    for dirt in dirts:
        player.dirtCollide(dirt)
        player.digCollide(dirt)
        if dirt.isDug == True:
            dirts.remove(dirt)
        for enemy in enemies:
            enemy.dirtCollide(dirt)
        for bullet in bullets:
            bullet.dirtCollide(dirt)
            bullet.screenCollide(size)
            bullet.playerCollide(player)
            if bullet.ded == True:
                bullets.remove(bullet)

    timer.update()
    lives.update(playerLives)
    levelnumberShow.update(levelNumber)
    
    if player.hit == True:
        if timer.value %2 == 0:
            if player.blinkFrame < 6:
                player.blinkImage()
            if player.blinkFrame == 6:
                player.hit = False
                player.blinkFrame = 0
                player.respawn()
        playerLives = player.lives

    player.move()
    for enemy in enemies:
        enemy.move()

    bgColor = r,g,b = 0,0,0
    screen.fill(bgColor)
    screen.blit(BG.image, BG.rect)
    for bullet in bullets:
        screen.blit(bullet.image, bullet.rect)
    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect)
    screen.blit(player.image, player.rect)
    for dirt in dirts:
        screen.blit(dirt.image, dirt.rect)
    screen.blit(timer.image, timer.rect)
    screen.blit(lives.image, lives.rect)
    screen.blit(levelnumberShow.image, levelnumberShow.rect)
    pygame.display.flip()
    clock.tick(60)
