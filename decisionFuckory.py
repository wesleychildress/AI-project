import random
#import numpy as np

#Decision Factory class
class decisionFuckory:
    def __init__ ( self, name= 'Davros' ):
        self.name = name
        self.directions = [ 'wait', 'up', 'down', 'right', 'left' ]
        self.last_result = 'Success'
        self.last_direction = 'down' #stores last direction moved
        self.switchx = 'right' #for switching directions left or right
        self.switchy = 'up' #for switching directions up or down
        self.pivot = 'up' #switching directions
        self.trackRow = 20 #for origin
        self.trackColumn = 20 #for origin
        self.trackMap = [['' for j in range(40)] for i in range(40)] #for keeping track of moves/walls

    # origin @ (20,20) in 40x40 2d array (i'm sure there is a more "intelligent" way of doing this)
    def put_trackMap_success(self): # keeping track of tiles visited placing a 1 on success
        if self.last_direction == "up":
            self.trackMap[self.trackRow-1][self.trackColumn] = 1
            self.trackRow = self.trackRow-1
        elif self.last_direction == "down":
            self.trackMap[self.trackRow+1][self.trackColumn] = 1
            self.trackRow = self.trackRow+1
        elif self.last_direction == "right":
            self.trackMap[self.trackRow][self.trackColumn+1] = 1
            self.trackColumn = self.trackColumn+1
        elif self.last_direction == "left":
            self.trackMap[self.trackRow][self.trackColumn-1] = 1
            self.trackColumn = self.trackColumn-1
        print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in self.trackMap]))

    def put_trackMap_wall(self): # keeping track of tiles of walls placing a 2
        if self.last_direction == "up":
            self.trackMap[self.trackRow-1][self.trackColumn] = 2
        elif self.last_direction == "down":
            self.trackMap[self.trackRow+1][self.trackColumn] = 2
        elif self.last_direction == "right":
            self.trackMap[self.trackRow][self.trackColumn+1] = 2
        elif self.last_direction == "left":
            self.trackMap[self.trackRow][self.trackColumn-1] = 2
        print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in self.trackMap]))

    def get_decision(self, verbose = True): #return move to framework
        return self.better_direction()

    def random_direction(self): #for random decision
        r = random.randint(1,4)
        self.last_direction = self.directions[r]
        return self.directions[r]

    def put_result(self, result): #keep track of last result
        self.last_result = result
        print "Result : " , self.last_result #to see last result

    def better_direction(self): # better than random decision
        print "last_direction: " , self.last_direction #to keep track of last directionself.
        print "last_result: " , self.last_result


        #Didn't hit a wall and last move wasn't a portal
        if self.last_result == 'Success': #basicly keep it moving until hits wall
            self.put_trackMap_success()
            #the main deal hear is the "pivot" if the agent can't traverse rows any longer
            if self.pivot == 'up': #traversing the tile map one row at a time moving upwards
                if self.last_direction == 'up': #('up')
                    if self.switchx == 'right':
                        self.switchx = 'left'
                        self.last_direction = self.directions[4]
                        return self.directions[4] #start moving to the left
                    elif self.switchx == 'left':
                        self.switchx = 'right'
                        self.last_direction = self.directions[3]
                        return self.directions[3] #start moving to the right
                else: #keeps moving up until hits wall
                    return self.last_direction
            if self.pivot == 'down': #traversing the tile map one row at a time in a downward motion
                if self.last_direction == 'down': #('down'):
                    if self.switchx == 'right':
                        self.switchx = 'left'
                        self.last_direction = self.directions[4]
                        return self.directions[4] #start moving to the left
                    elif self.switchx == 'left':
                        self.switchx = 'right'
                        self.last_direction = self.directions[3]
                        return self.directions[3] #start moving right
                else: #keeps going down until hits wall
                    return self.last_direction
            if self.pivot == 'right': #traversing the tile map one column at a time heading right
                if self.last_direction == 'right': #('right'):
                    if self.switchy == 'up':
                        self.switchy = 'down'
                        self.last_direction = self.directions[2]
                        return self.directions[2] #start moving downward
                    elif self.switchy == 'down':
                        self.switchy = 'up'
                        self.last_direction = self.directions[1]
                        return self.directions[1] #start moving upward
                else: #keeps going right until hits wall
                    return self.last_direction
            if self.pivot == 'left': #traversing the tile map one column at a time heading left
                if self.last_direction == 'left': #('left'):
                    if self.switchy == 'up':
                        self.switchy = 'down'
                        self.last_direction = self.directions[2]
                        return self.directions[2] #start moving downward
                    elif self.switchy == 'down':
                        self.switchy = 'up'
                        self.last_direction = self.directions[1]
                        return self.directions[1] #start moving upward
                else: #keeps going left until hits wall
                    return self.last_direction

        if self.last_result == 'wall': #these functions change stuff up to change row,column, or direction
            self.put_trackMap_wall()
            if self.pivot == 'up': #traversing the tile map one row at a time moving upwards
                if self.last_direction == 'up': #can't search rows upwards any longer
                    self.trackRow = 20 #reset row origin
                    self.trackColumn = 20 #reset column origin
                    self.trackMap = [['' for j in range(40)] for i in range(40)] #clear the "trackMap"
                    self.pivot = 'down' #switch the piviot to search rows heading downwards
                    self.last_direction = self.directions[2]
                    return self.directions[2]
                elif self.last_direction == 'down': #this is just here to get agent down as far as possible before searching rows up
                    if self.switchx == 'right':
                        self.switchx = 'left'
                        self.last_direction = self.directions[4]
                        return self.directions[4] #start moving left
                    elif self.switchx == 'left':
                        self.switchx = 'right'
                        self.last_direction = self.directions[3]
                        return self.directions[3] #start moving right
                elif self.last_direction == 'left' or 'right' : #hits wall so move up a row
                    self.last_direction = self.directions[1]
                    return self.directions[1]
                else:
                    oops = self.random_direction() #if all else fails generate a random decision
                    return oops
            if self.pivot == 'down':
                if self.last_direction == 'down': #can't search rows downwards any longer
                    self.trackRow = 20 #reset row origin
                    self.trackColumn = 20 #reset column origin
                    self.trackMap = [['' for j in range(40)] for i in range(40)]
                    self.pivot = 'right' #switch the piviot to search columns heading right
                    self.last_direction = self.directions[1]
                    return self.directions[1] #******************** where comments stop ********************************
                elif self.last_direction == 'up':
                    if self.switchx == 'right':
                        self.switchx = 'left'
                        self.last_direction = self.directions[4]
                        return self.directions[4] #moves in new direction
                    elif self.switchx == 'left':
                        self.switchx = 'right'
                        self.last_direction = self.directions[3]
                        return self.directions[3] #moves in new direction
                elif self.last_direction == 'left' or 'right' :
                    self.last_direction = self.directions[2]
                    return self.directions[2]
                else:
                    oops = self.random_direction() #if all else fails generate a random decision
                    return oops
            if self.pivot == 'right':
                if self.last_direction == 'right':
                    self.trackRow = 20
                    self.trackColumn = 20
                    self.trackMap = [['' for j in range(40)] for i in range(40)]
                    self.pivot = 'left'
                    self.last_direction = self.directions[4]
                    return self.directions[4]
                elif self.last_direction == 'left':
                    if self.switchy == 'up':
                        self.switchy = 'down'
                        self.last_direction = self.directions[2]
                        return self.directions[2] #moves in new direction
                    elif self.switchy == 'down':
                        self.switchy = 'up'
                        self.last_direction = self.directions[1]
                        return self.directions[1] #moves in new direction
                elif self.last_direction == 'up' or 'down' :
                    self.last_direction = self.directions[3]
                    return self.directions[3]
                else:
                    oops = self.random_direction() #if all else fails generate a random decision
                    return oops
            if self.pivot == 'left':
                if self.last_direction == 'left':
                    self.trackRow = 20
                    self.trackColumn = 20
                    self.trackMap = [['' for j in range(40)] for i in range(40)]
                    self.pivot = 'up'
                    self.last_direction = self.directions[1]
                    return self.directions[1]
                elif self.last_direction == 'right':
                    if self.switchy == 'up':
                        self.switchy = 'down'
                        self.last_direction = self.directions[2]
                        return self.directions[2] #moves in new direction
                    elif self.switchy == 'down':
                        self.switchy = 'up'
                        self.last_direction = self.directions[1]
                        return self.directions[1] #moves in new direction
                elif self.last_direction == 'up' or 'down' :
                    self.last_direction = self.directions[4]
                    return self.directions[4]
                else:
                    oops = self.random_direction() #if all else fails generate a random decision
                    return oops

        else:
            oops = self.random_direction()
            return oops
