"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
import random
from decisionFactory import decisionFactory
#from character import Character
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
MAPSIZE = 10
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = [[1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]]





# Character Class
class Character(object):                    #Characters can move around and do cool stuff
    def __init__(self, Column, Row, Name= 'Davros' ):
        self.Name = Name
        self.Column = Column
        self.Row = Row
        
    def Move(self, decision):

        
        if decision == "up":
            if self.Row > 0:                #If within boundaries of grid
                if self.CollisionCheck("up") == False:       #And nothing in the way
                    self.Row -= 1            #Go ahead and move

        elif decision == "down":
            if self.Row < MAPSIZE-1:
                if self.CollisionCheck("down") == False:
                    self.Row += 1
                    
        elif decision == "right":
            if self.Column < MAPSIZE-1:
                if self.CollisionCheck("right") == False:
                         self.Column += 1
        
        elif decision == "left":
            if self.Column > 0:
                if self.CollisionCheck("left") == False:
                    self.Column -= 1


    def CollisionCheck(self, decision):       #Checks to see if the movement goes into a wall
        if decision == "up":
            if grid[(self.Row)-1][self.Column] == 1:
                return True
        elif decision == "left":
            if grid[self.Row][(self.Column)-1] == 1:
                return True
        elif decision == "right":
            if grid[self.Row][(self.Column)+1] == 1:
                return True
        elif decision == "down":
            if grid[(self.Row)-1][self.Column] == 1:
                return True
        return False

    








#for row in range(10):
#    # Add an empty array that will hold each cell
#    # in this row
#    grid.append([])
#    for column in range(10):
#        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
#grid[1][5] = 1

# Setting portal to random coordinate
RandomRow = random.randint(1, MAPSIZE - 2)  
RandomColumn = random.randint(1, MAPSIZE - 2)
grid[RandomRow][RandomColumn] = 2

# Setting character to random coordinate
RandomRowChar = random.randint(1, MAPSIZE - 2)  
RandomColumnChar = random.randint(1, MAPSIZE - 2)

#Checking if the character was placed in the same position as the portal
while(grid[RandomRowChar][RandomColumnChar] == 2):
    RandomRowChar = random.randint(1, MAPSIZE - 2)  
    RandomColumnChar = random.randint(1, MAPSIZE - 2)
Hero = Character(RandomColumnChar, RandomRowChar, 'Hero')
DF = decisionFactory('Hero')


# Initialize pygame
pygame.init()

# Initialize decisionFactory
df = decisionFactory()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Random Decision-Making")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        
     
    decision = DF.get_decision()
    #DF.put_decision(result)


    if decision == "up":
        Hero.Move("up")
    if decision == "down":
        Hero.Move("down")
    if decision == "left":
        Hero.Move("left")
    if decision == "right":
        Hero.Move("right")
    
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(MAPSIZE):
        for column in range(MAPSIZE):
            color = WHITE
            if grid[row][column] == 1:
                color = RED
            if grid[Hero.Row][Hero.Column] == 0:    
                color= BLUE
            #if grid[row][column] == 2:  #portal
            #    color = BLUE
            #if grid[row][column] == 3:  #Character       
            #    color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
#Be IDLE friendly. If you forget this line, the program will 'hang'
#on exit.
pygame.quit()