import random 
#import numpy as np

#Decision Factory class
class decisionFactory:
    def __init__ ( self, name= 'Davros' ):
        self.name = name
        self.directions = [ 'wait', 'up', 'down', 'right', 'left' ]
        self.last_result = 'Success'
        self.last_direction = 'wait' #stores last direction moved 
      
        #relative position
        #self.state.pos = (0,0)
    
    def get_decision(self, verbose = True):
        return self.better_direction()
    
    def random_direction(self):
        #wait state
        # r = random.randint(0,4)
        r = random.randint(1,4)
    
        self.last_direction = self.directions[r]
    
        return self.directions[r]

   
        
  
        #better than random - doesn't let it go back to a previous spot if portal isn't there
        #range library fuction generates numbers from 1st argument to number before second
        #so range(3,5) will generate 3,4 
        #For team - in wall case it could also check if last last result == wall - indicating a corner and have other options there but im a little stuck there. 
    def better_direction(self):
        r = random.randint(1,4) #same as random_direction
        case = self.last_result #checks to store last result
        print "last_direction: " , self.last_direction #to keep track of last direction
        if case == 'wall':
            if self.last_direction == 'up':
                shift = random.randint(3,4)  #dont let it go "down - 1 up - 2" since no portal is in last direction and wall in this direction
                return self.directions[shift] #moves in new direction
        
            elif self.last_direction == 'down': 
                shift = random.randint(3,4); #dont let it go "up - 1 2 - down" since no portal is in last direction and wall in this direction
                self.last_direction = self.directions[shift] 
                return self.directions[shift]
    
            elif self.last_direction == 'left' : 
                shift = random.randint(1,2) #dont let it go "right - 3 left - 4" since no portal is in last direction and wall in this direction
                return self.directions[shift]
    
            elif self.last_direction == 'right': 
                shift = random.randint(1,2); #dont let it go "left - 4 or right-3" since no portal in last direction and wall in this direction
                self.last_direction = self.directions[shift]
                return self.directions[shift]
            else:
                self.last_direction = self.directions[r]
                return self.directions[r]
            
            
           #Didn't hit a wall and last move wasn't a portal 
        if case == 'Success':
            if self.last_direction == 'up' : #succesfully but last direction - no portal
                choices = range(1,2) + range (3,5) #dont allow it to go back "down - 2" since theres no portal in that direction
                shift = random.choice(choices) #chooses new direction in restricted range
                self.last_direction = self.directions[shift]#store new direction in last_direction
                return self.directions[shift] #move to new direction
        
            elif self.last_direction == 'down':
                shift = random.randint(2,4); #dont allow it to go "up - 1" back since theres no portal in that direction
                self.last_direction = self.directions[shift] 
                return self.directions[shift] 
    
            elif self.last_direction == 'left' : 
                choices = range(1,3) + range (4,5) #dont let it go "3-right" since no portal is in that postion
                shift = random.choice(choices) 
                self.last_direction = self.directions[shift]
                return self.directions[shift] 
    
            elif self.last_direction == 'right' : 
                shift = random.randint(1,3); #dont let it go "left - 4" since no portal is in that postion
                self.last_direction = self.directions[shift]
                return self.directions[shift]
            else:
                self.last_direction = self.directions[r]
                return self.directions[r]
        
    def put_result(self, result):
        self.last_result = result
        print "Result : " , self.last_result #to see last result
        
  
        
