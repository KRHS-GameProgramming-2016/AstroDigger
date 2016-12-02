import pygame, sys, math
from Dirt import *
class Level():
    def __init__(self, levelFile, tileSize=64):
        self.walls = []
        self.players = []
        #self.ballSpawns = []
        self.tileSize = tileSize
        
        self.loadLevel(levelFile)
        
    def unloadLevel(self): 
        self.walls = []
        self.players = []
        self.ballSpawns = []
               
    def loadLevel(self, levelFile):        
        f = open("Resources/Levels/" + levelFile)
        lines = f.readlines()
        f.close()
