import pygame, sys, math
from dirt import *
from diggerlevel1 import *
class Level():
    def __init__(self, levelFile, tileSize=64):
        self.dirt = []
        self.players = []
        self.playerSpawns = []
        self.tileSize = tileSize
        
        self.loadLevel(levelFile)
        
    def unloadLevel(self): 
        self.dirt = []
        self.players = []
        self.ballSpawns = []
               
    def loadLevel(self, levelFile):        
        f = open("rsc/levels/"+levelFile, 'r')
        lines = f.readlines()
        f.close()




*            *
*            *
* a          *
*111111111111*
*111111111111*
*11 x 1111111*
*111111111111*
*11111111 x 1*
*111111111111*
*111111111111*

