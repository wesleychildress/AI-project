import random 
#import numpy as np

#Decision Factory class
class decisionFactory:
    def __init__ ( self, name= 'Davros' ):
        self.name = name
        self.directions = [ 'wait', 'up', 'down', 'right', 'left' ]
        self.last_result = 'Success'
        self.last_direction = 'up' #stores last direction moved
        self.test = False #switching directions
        self.switchx = False #switching directions
        self.switchy = False #switching directions
        self.toggle = False 
        #relative position
        #self.state.pos = (0,0)
    
    def get_decision(self, verbose = True):
        return self.search_pattern()
    
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
        
  
        

    
    # Want to keep going in a certain direction until it hits a wall, then to change the 
    # direction to either adjacent sides and go back the opposite direction.
    # So, in an essence it will be snaking through the maze.
    
    def search_pattern(self):
        
        case = self.last_result #checks to store last result
        # In the beginning of execution pulls hard code value from the          
        # last_direction
        if case == 'Success':
            if self.test == True:
                if self.toggle == False:
                    if self.switchx == True:
                        self.last_direction = 'down'
                        self.test = False 
                        return self.directions[2]
                    elif self.switchx == False:
                        self.last_direction = 'up'
                        self.test = False
                        return self.directions[1]
                    
                elif self.toggle == True:
                    if self.switchy == True:
                        self.last_direction = 'left'
                        self.test = False 
                        return self.directions[4]
                    elif self.switchy == False:
                        self.last_direction = 'right'
                        self.test = True 
                        return self.directions[3]
            else:
                self.test = False
                return self.last_direction
        
        if case == 'wall':
            if self.last_direction == 'up':
                self.test = True
                self.switchx = True
                # returning going right
                self.last_direction = 'right'
                return self.directions[3]
            
            elif self.last_direction == 'down':
                self.test = True
                self.switchx = False   
                # returning going right
                self.last_direction = 'right'
                return self.directions[3]
            
            elif self.last_direction == 'right':
                self.test = True 
                self.switchy = True
                self.toggle = True
                self.last_direction = 'up'
                return self.directions[2]
            
            elif self.last_direction == 'left':
                self.test = True
                self.switchy = False
                self.toggle = True 
                self.last_direction  = 'down'
                return self.directions[2]
            
                
