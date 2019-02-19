#!/usr/bin/env python

import random
import pygame, sys
from pygame.locals import *
import decisionFactory as DF

#colors
BLACK = (0, 0, 0 )
RED = (255, 0, 0 ) #walls
WHITE = (255, 255, 255 ) #open space
BLUE = (0, 0, 225 ) #hero
GREEN = (0, 255, 0 ) #portal

#game dimensions
tileSize = 60       #pixel sizes for grid squares
mapSize = 10        #M x M mapSize

#numbers representing
FLOOR = 0
WALL = 1
HERO = 2
PORTAL = 3

#linking colors and numbers
colors = {
           FLOOR : WHITE,
           WALL : RED,
           HERO : BLUE,
           PORTAL : GREEN }

# boolean
Done = False

#setting up display
pygame.init()
screen = pygame.display.set_mode((mapSize * tileSize, mapSize * tileSize))

#Decision Factory class
class decisionFactory:
    def __init__ ( self, name= 'Davros' ):
        self.name = name
        self.directions = [ 'wait', 'up', 'down', 'right', 'left' ]
        self.last_result = 'sucess'
        self.last_direction = 'wait'
        #relative position
        #self.state.pos = (0,0)

    def get_decision(self, verbose = True):
        return self.random_direction()

    def random_direction(self):
        #wait state
        r = random.randint(1,4)
        #r = random.rantint(1,4)

        self.last_direction = self.directions[r]

        return self.directions[r]

    def put_result(self, result):
        self.last_result = put_result

class moveHero():                    #Characters can move around and do cool stuff

    def Move(self, decision):

        if decision == "up":
            if self.CollisionCheck("up") == False:          #And nothing in the way
                    if self.PortalCheck("up") == False:     #No Portal
                        Map.tileMap[heroRow+1][heroColumn] = 2
                        Map.tileMap[heroRow][heroColumn] = 0
                        Map.heroRow = heroRow+1
                    elif self.PortalCheck("up") == True:
                        Done = True

        elif decision == "down":
            if self.CollisionCheck("down") == False:          #And nothing in the way
                    if self.PortalCheck("down") == False:     #No Portal
                        Map.tileMap[heroRow-1][heroColumn] = 2
                        Map.tileMap[heroRow][heroColumn] = 0
                        Map.heroRow = heroRow-1
                    elif self.PortalCheck("down") == True:
                        Done = True

        elif decision == "right":
            if self.CollisionCheck("right") == False:          #And nothing in the way
                    if self.PortalCheck("right") == False:     #No Portal
                        Map.tileMap[heroRow][heroColumn+1] = 2
                        Map.tileMap[heroRow][heroColumn] = 0
                        Map.heroColumn = heroColumn+1
                    elif self.PortalCheck("right") == True:
                        Done = True

        elif decision == "left":
            if self.CollisionCheck("left") == False:          #And nothing in the way
                    if self.PortalCheck("left") == False:     #No Portal
                        Map.tileMap[heroRow][heroColumn-1] = 2
                        Map.tileMap[heroRow][heroColumn] = 0
                        Map.heroColumn = heroColumn-1
                    elif self.PortalCheck("left") == True:
                        Done = True

    def CollisionCheck(self, decision):       #Checks if anything is on top of the grass in the direction that the character wants to move. Used in the move function
        if decision == "up":
            if Map.tileMap[heroRow+1][heroColumn] == 1:
                return True
        elif decision == "down":
            if Map.tileMap[heroRow-1][heroColumn] == 1:
                return True
        elif decision == "right":
            if Map.tileMap[heroRow][heroColumn+1] == 1:
                return True
        elif decision == "left":
            if Map.tileMap[heroRow][heroColumn-1] == 1:
                return True
        return False

    def PortalCheck(self, decision):       #Checks if anything is on top of the grass in the direction that the character wants to move. Used in the move function
        if decision == "up":
            if Map.tileMap[heroRow+1][heroColumn] == 3:
                return True
        elif decision == "down":
            if Map.tileMap[heroRow-1][heroColumn] == 3:
                return True
        elif decision == "right":
            if Map.tileMap[heroRow][heroColumn+1] == 3:
                return True
        elif decision == "left":
            if Map.tileMap[heroRow][heroColumn-1] == 3:
                return True
        return False

class Map(object):              #The main class
    global mapSize
    global heroRow
    global heroColumn
    global portalRow
    global portalColumn

    #our map
    tileMap = [
                [1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1]
            ]

    randomHeroRow = random.randint(1, mapSize - 2)      #Dropping the hero in
    randomHeroColumn = random.randint(1, mapSize - 2)
    tileMap[randomHeroRow][randomHeroColumn] = 2
    heroRow = randomHeroRow
    heroColumn = randomHeroColumn

    while True:
        randomPortalRow = random.randint(1, mapSize - 2)      #Dropping the hero in
        randomPortalColumn = random.randint(1, mapSize - 2)
        if randomPortalRow != randomHeroRow & randomPortalColumn != randomHeroColumn:
            break

    tileMap[randomPortalRow][randomPortalColumn] = 3
    portalRow = randomPortalRow
    portalColumn = randomPortalColumn


Map = Map()
DF = decisionFactory()
turd = moveHero()

while not Done:     #Main pygame loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True
            sys.exit()

    decision = DF.get_decision()

    if decision == "up":
        turd.Move("up")
    if decision == "down":
        turd.Move("down")
    if decision == "left":
        turd.Move("left")
    if decision == "right":
        turd.Move("right")

    for row in range(mapSize):
        for column in range (mapSize):
            pygame.draw.rect(screen, colors[Map.tileMap[row][column]], (column * tileSize, row * tileSize, tileSize, tileSize))

    #update display
    pygame.display.update()
