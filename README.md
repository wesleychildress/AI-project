AI-project

Better than random:

The idea I was going with is to use last direction and keep track of if there was a portal in that previous direction or not and if there wasn't to remove that direction from the next possible choices. For example if last direction was "up" and the portal was not in that location then the bot should only have the options to go down, right or left because returning to the last position is useless since you already know that the portal isn't there.

Issues:
I'm not sure completely sure if the portal check is checking the last location and returning that or the current location that the actor is actually on. I copied the structure of self.last_direction in the decisionfactory class so i think it is but someone double check.
Also it seems skewed to moving to the right side of the grid and i think that might have to do with random when one of the choices is elimated. like for example In the cases of up or down it has more of a likely chance to generate a 3 - 4 and i think thats affecting it. Could be wrong tho
