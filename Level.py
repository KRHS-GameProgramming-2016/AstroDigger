import pygame, sys, math
from Dirt import *
from Enemy import *

class Level():
    def __init__(self, levelFile, levelNumber=1, tileSize=64):
        self.dirts = []
        self.players = []
        self.enemies = []
        self.playerSpawns = []
        self.tileSize = tileSize
        
        self.loadLevel(levelFile, levelNumber)
        
    def unloadLevel(self): 
        self.dirts = []
        self.player = []
        self.enemySpawn = []
               
    def loadLevel(self, levelFile, levelNumber):        
        f = open("Resources/Levels/"+levelFile)
        lines = f.readlines()
        f.close()
        
        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline += c
            newlines += [newline]
            
        lines = newlines
            
        startIndex = lines.index(str(levelNumber))+1
        endIndex = startIndex + 10    
        
        newlines = []
        for line in range(startIndex, endIndex):
            #print lines[line]
            newlines += [lines[line]]
        lines = newlines
        
        for line in lines:
            print line
        
        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c in "12345" :       #levels of dirt
                    self.dirts += [Dirt(c, 
                                       [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  ]
        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c in "x" :       #enemies
                    self.enemies += [Enemy("Enemy-Pew Left.png", 
                                       [0,0],
                                       [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  ]
        
        

if __name__ == "__main__":
    level = Level("Digger level1.lvl", 1)
