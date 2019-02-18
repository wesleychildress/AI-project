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

while True:
     randomPortalRow = random.randint(1, mapSize - 2)      #Dropping the hero in
     randomPortalColumn = random.randint(1, mapSize - 2)
     if randomPortalRow != randomHeroRow & randomPortalColumn != randomHeroColumn:
        break

tileMap[randomPortalRow][randomPortalColumn]=3

#setting up display
pygame.init()
screen = pygame.display.set_mode((mapSize * tileSize, mapSize * tileSize))

while not Done:     #Main pygame loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True
            sys.exit()
    decision = DF.get_decision()

    for row in range(mapSize):
        for column in range (mapSize):
            pygame.draw.rect(screen, colors[tileMap[row][column]], (column * tileSize, row * tileSize, tileSize, tileSize))

    #update display
    pygame.display.update()
