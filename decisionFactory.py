import random 
#import numpy as np

#Decision Factory class
class DecisionFactory:
    def __init__ ( self, name= 'Davros' ):
        self.name = name
        self.directions = [ 'wait', 'up', 'down', 'right', 'left' ]
        self.last_result = 'sucess'
        self.last_direction = 'wait'
        #relative position
        self.state.pos = (0,0)
    
    def get_decision(self, verbose = True):
        return self.random_direction()
    
    def random_direction(self):
        #wait state
        # r = random.randint(0,4)
        r = random.rantint(1,4)
    
        self.last_direction = self.directions[r]
    
        return self.directions[r]

    def put_result(self, result):
        self.last_result = result
