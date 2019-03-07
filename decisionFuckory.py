import random
#import numpy as np

#Decision Factory class
class decisionFuckory:
    def __init__ ( self, name= 'Davros' ):
        self.name = name
        self.directions = [ 'wait', 'up', 'down', 'right', 'left' ]
        self.last_result = 'Success'
        self.last_direction = 'down' #stores last direction moved
        self.switchx = 'right' #switching directions
        self.switchy = 'up'
        self.pivot = 'up' #switching directions
        self.trackRow = 20
        self.trackColumn = 20
        self.trackMap = [['' for j in range(40)] for i in range(40)]

    def put_trackMap_success(self):
        if self.last_direction == "up":
            self.trackMap[self.trackRow-1][self.trackColumn] = 1
            self.trackRow = self.trackRow-1
        elif self.last_direction == "down":          #And nothing in the way
            self.trackMap[self.trackRow+1][self.trackColumn] = 1
            self.trackRow = self.trackRow+1
        elif self.last_direction == "right":
            self.trackMap[self.trackRow][self.trackColumn+1] = 1
            self.trackColumn = self.trackColumn+1
        elif self.last_direction == "left":
            self.trackMap[self.trackRow][self.trackColumn-1] = 1
            self.trackColumn = self.trackColumn-1
        print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in self.trackMap]))

    def put_trackMap_wall(self):
        if self.last_direction == "up":
            self.trackMap[self.trackRow-1][self.trackColumn] = 2
            #self.trackRow = self.trackRow-1
        elif self.last_direction == "down":          #And nothing in the way
            self.trackMap[self.trackRow+1][self.trackColumn] = 2
            #self.trackRow = self.trackRow+1
        elif self.last_direction == "right":
            self.trackMap[self.trackRow][self.trackColumn+1] = 2
            #self.trackColumn = self.trackColumn+1
        elif self.last_direction == "left":
            self.trackMap[self.trackRow][self.trackColumn-1] = 2
            #self.trackColumn = self.trackColumn-1
        print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in self.trackMap]))

    def get_decision(self, verbose = True):
        return self.better_direction()

    def random_direction(self):
        r = random.randint(1,4)
        self.last_direction = self.directions[r]
        return self.directions[r]

    def put_result(self, result):
        self.last_result = result
        print "Result : " , self.last_result #to see last result

    def better_direction(self):
        print "last_direction: " , self.last_direction #to keep track of last directionself.
        print "last_result: " , self.last_result

        if self.last_result == 'Success':
            self.put_trackMap_success()
            #Didn't hit a wall and last move wasn't a portal
            if self.pivot == 'up':
                if self.last_direction == 'up': #('up' or 'down'):
                    if self.switchx == 'right':
                        self.switchx = 'left'
                        self.last_direction = self.directions[4]
                        return self.directions[4] #moves in new direction
                    elif self.switchx == 'left':
                        self.switchx = 'right'
                        self.last_direction = self.directions[3]
                        return self.directions[3] #moves in new direction
                else:
                    return self.last_direction
            if self.pivot == 'down':
                if self.last_direction == 'down': #('up' or 'down'):
                    if self.switchx == 'right':
                        self.switchx = 'left'
                        self.last_direction = self.directions[4]
                        return self.directions[4] #moves in new direction
                    elif self.switchx == 'left':
                        self.switchx = 'right'
                        self.last_direction = self.directions[3]
                        return self.directions[3] #moves in new direction
                else:
                    return self.last_direction
            if self.pivot == 'right':
                if self.last_direction == 'right': #('up' or 'down'):
                    if self.switchy == 'up':
                        self.switchy = 'down'
                        self.last_direction = self.directions[2]
                        return self.directions[2] #moves in new direction
                    elif self.switchy == 'down':
                        self.switchy = 'up'
                        self.last_direction = self.directions[1]
                        return self.directions[1] #moves in new direction
                else:
                    return self.last_direction
            if self.pivot == 'left':
                if self.last_direction == 'left': #('up' or 'down'):
                    if self.switchy == 'up':
                        self.switchy = 'down'
                        self.last_direction = self.directions[2]
                        return self.directions[2] #moves in new direction
                    elif self.switchy == 'down':
                        self.switchy = 'up'
                        self.last_direction = self.directions[1]
                        return self.directions[1] #moves in new direction
                else:
                    return self.last_direction

        if self.last_result == 'wall':
            self.put_trackMap_wall()
            if self.pivot == 'up':
                if self.last_direction == 'up':
                    self.trackRow = 20
                    self.trackColumn = 20
                    self.trackMap = [['' for j in range(40)] for i in range(40)]
                    self.pivot = 'down'
                    self.last_direction = self.directions[2]
                    return self.directions[2]
                elif self.last_direction == 'down':
                    if self.switchx == 'right':
                        self.switchx = 'left'
                        self.last_direction = self.directions[4]
                        return self.directions[4] #moves in new direction
                    elif self.switchx == 'left':
                        self.switchx = 'right'
                        self.last_direction = self.directions[3]
                        return self.directions[3] #moves in new direction
                elif self.last_direction == 'left' or 'right' :
                    self.last_direction = self.directions[1]
                    return self.directions[1]
                else:
                    oops = self.random_direction()
                    return oops
            if self.pivot == 'down':
                if self.last_direction == 'down':
                    self.trackRow = 20
                    self.trackColumn = 20
                    self.trackMap = [['' for j in range(40)] for i in range(40)]
                    self.pivot = 'right'
                    self.last_direction = self.directions[1]
                    return self.directions[1]
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
                    oops = self.random_direction()
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
                    oops = self.random_direction()
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
                    oops = self.random_direction()
                    return oops

        else:
            oops = self.random_direction()
            return oops
