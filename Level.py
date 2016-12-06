import pygame, sys, math
from Dirt import *

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
        f = open("Resources/Levels/"+levelFile)
        lines = f.readlines()
        f.close()
