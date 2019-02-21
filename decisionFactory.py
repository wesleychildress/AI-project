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

   
        
  
        #better than random
        #not a 100% sure about the range to exclude the one direction you dont want rn
    def better_direction(self):
        r = random.randint(1,4)
        case = self.last_result #checks to see last result
        if case == 'wall':
            if self.last_direction == 'up': #if it hits a wall
                shift = 2; #just going the oppsite direction rn if it hits a wall(want to fix after 'Success' case)
                print "last_direction: " , self.last_direction
                self.last_direction = self.directions[shift]#change direction down...
                return self.directions[shift]
        
            elif self.last_direction == 'down': #if it hits a wall
                shift = 1; #just going the oppsite direction rn if it hits a wall(want to fix after 'Success' case)
                print "last_direction: " , self.last_direction
                self.last_direction = self.directions[shift]#change direction up...
                return self.directions[shift]
    
            elif self.last_direction == 'left' : #if it hits a wall
                shift = 3; #just going the oppsite direction rn if it hits a wall(want to fix after 'Success' case)
                print "last_direction: " , self.last_direction
                self.last_direction = self.directions[shift]#change direction right...
                return self.directions[shift]
    
            elif self.last_direction == 'right': #if it hits a wall
                shift = 4; #just going the oppsite direction rn if it hits a wall(want to fix after 'Success' case)
                print "last_direction: " , self.last_direction
                self.last_direction = self.directions[shift]#change direction left...
                return self.directions[shift]
            else:
                print "last_direction: " , self.last_direction
                self.last_direction = self.directions[r]
                return self.directions[r]
            #good to move
        if case == 'Success':
            if self.last_direction == 'up' : #succesfully but last direct - no portal
                choices = range(1,2) + range (3,5) #dont allow it to go "down" back since theres no portal in that direction
                #not a 100% sure about the range to exclude the one direction you dont want rn
                shift = random.choice(choices)
                print "last_direction: " , self.last_direction
                self.last_direction = self.directions[shift]#change direction 
                return self.directions[shift]
        
            elif self.last_direction == 'down':#succesfully but last direct no portal
                shift = random.randint(2,4); #dont allow it to go "up" back since theres no portal in that direction
                print "last_direction: " , self.last_direction
                self.last_direction = self.directions[shift] 
                return self.directions[shift] #change direction 
    
            elif self.last_direction == 'left' : #succesfully but last direct no portal
                choices = range(1,3) + range (4)
                shift = random.choice(choices) #dont let it go "right" since no portal is in that postion
                self.last_direction = self.directions[shift]
                return self.directions[shift] #change direction right..
    
            elif self.last_direction == 'right' : #succesfully but last direct no portal
                shift = random.randint(1,3); #dont let it go "left" since no portal is in that postion
                print "last_direction: " , self.last_direction
                self.last_direction = self.directions[shift]
                return self.directions[shift]#change direction right..
            else:
                print "last_direction: " , self.last_direction
                self.last_direction = self.directions[r]
                return self.directions[r]
        
    def put_result(self, result):
        self.last_result = result
        print "Result : " , self.last_result #to see result
        
  
        
