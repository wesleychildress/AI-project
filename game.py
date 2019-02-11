#!/usr/bin/env python

import random
import pygame
from pygame.base import *

pygame.init()                                 #start up dat pygame
clock = pygame.time.Clock()                   #for framerate or something? still not very sure
Screen = pygame.display.set_mode([650, 650])  #making the window
Done = False                                  #variable to keep track if window is open
MapSize = 10                                  #how many tiles in either Dof grid

TileWidth = 60                                #pixel sizes for grid squares
TileHeight = 60
TileMargin = 4

BLACK = (0, 0, 0)                             #some color definitions
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

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
        r = random.randint(0,4)
        #r = random.rantint(1,4)

        self.last_direction = self.directions[r]

        return self.directions[r]

    def put_result(self, result):
        self.last_result = result

class MapTile(object):                       #The main class for stationary things that inhabit the grid ... grass, trees, rocks and stuff.
    def __init__(self, Name, Column, Row):
        self.Name = Name
        self.Column = Column
        self.Row = Row



class Character(object):                    #Characters can move around and do cool stuff
    def __init__(self, Name, HP, Column, Row):
        self.Name = Name
        self.HP = HP
        self.Column = Column
        self.Row = Row

    def Move(self, decision):


        if decision == "up":
            if self.Row > 0:                #If within boundaries of grid
                if self.CollisionCheck("up") == False:       #And nothing in the way
                    self.Row -= 1            #Go ahead and move

        elif decision == "down":
            if self.Row < MapSize-1:
                if self.CollisionCheck("down") == False:
                    self.Row += 1

        elif decision == "right":
            if self.Column < MapSize-1:
                if self.CollisionCheck("right") == False:
                         self.Column += 1

        elif decision == "left":
            if self.Column > 0:
                if self.CollisionCheck("left") == False:
                    self.Column -= 1

        Map.update()

    def CollisionCheck(self, decision):       #Checks if anything is on top of the grass in the direction that the character wants to move. Used in the move function
        if decision == "up":
            if len(Map.Grid[self.Column][(self.Row)-1]) > 1:
                return True
        elif decision == "left":
            if len(Map.Grid[self.Column-1][(self.Row)]) > 1:
                return True
        elif decision == "right":
            if len(Map.Grid[self.Column+1][(self.Row)]) > 1:
                return True
        elif decision == "down":
            if len(Map.Grid[self.Column][(self.Row)+1]) > 1:
                return True
        return False

    def Location(self):
        print("Coordinates: " + str(self.Column) + ", " + str(self.Row))


class Map(object):              #The main class; where the action happens
    global MapSize

    Grid = []

    for Row in range(MapSize):     # Creating grid
        Grid.append([])
        for Column in range(MapSize):
            Grid[Row].append([])

    for Row in range(MapSize):     #Filling grid with grass
        for Column in range(MapSize):
            TempTile = MapTile("Grass", Column, Row)
            Grid[Column][Row].append(TempTile)

    for Row in range(MapSize):     #Putting some rocks near the top
        for Column in range(MapSize):
            TempTile = MapTile("Rock", Column, Row)
            if Row == 0 or Row == 9:
                Grid[Column][Row].append(TempTile)

    for Column in range(MapSize):     #Putting some rocks near the top
        for Row in range(1, 9):
            TempTile = MapTile("Rock", Column, Row)
            if Column == 0 or Column == 9:
                Grid[Column][Row].append(TempTile)

    RandomRow = random.randint(0, MapSize - 1)      #Dropping the hero in
    RandomColumn = random.randint(0, MapSize - 1)
    Hero = Character("Hero", 10, RandomColumn, RandomRow)

    def update(self):        #Very important function
                             #This function goes through the entire grid
                             #And checks to see if any object's internal coordinates
                             #Disagree with its current position in the grid
                             #If they do, it removes the objects and places it
                             #on the grid according to its internal coordinates

        for Column in range(MapSize):
            for Row in range(MapSize):
                for i in range(len(Map.Grid[Column][Row])):
                    if Map.Grid[Column][Row][i].Column != Column:
                        Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                    elif Map.Grid[Column][Row][i].Name == "Hero":
                        Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
        Map.Grid[int(Map.Hero.Column)][int(Map.Hero.Row)].append(Map.Hero)

Map = Map()
DF = decisionFactory()

while not Done:     #Main pygame loop

    for event in pygame.event.get():         #catching events
        if event.type == pygame.QUIT:
            Done = True
    decision = DF.get_decision()
    #DF.put_decision(result)


    if decision == "up":
        Map.Hero.Move("up")
    if decision == "down":
        Map.Hero.Move("down")
    if decision == "left":
        Map.Hero.Move("left")
    if decision == "right":
        Map.Hero.Move("right")

    Screen.fill(BLACK)

    for Row in range(MapSize):           # Drawing grid
        for Column in range(MapSize):
            for i in range(0, len(Map.Grid[Column][Row])):
                Color = WHITE
                if len(Map.Grid[Column][Row]) == 2:
                    Color = RED
                if Map.Grid[Column][Row][i].Name == "Hero":
                    Color = GREEN


            pygame.draw.rect(Screen, Color, [(TileMargin + TileWidth) * Column + TileMargin,
                                             (TileMargin + TileHeight) * Row + TileMargin,
                                             TileWidth,
                                             TileHeight])

    clock.tick(60)      #Limit to 60 fps or something

    pygame.display.flip()     #Honestly not sure what this does, but it breaks if I remove it
    Map.update()

pygame.quit()
