AI-project

Better than random:

The idea I was going with is to use last direction and keep track of if there was a portal in that previous direction or not and if there wasn't to remove that direction from the next possible choices. For example if last direction was "up" and the portal was not in that location then the bot should only have the options to go down, right or left because returning to the last position is useless since you already know that the portal isn't there and for walls to not give it the option to go back to the last move or up into the wall again. Also changed the messages the framework is sending according to the textbook

Issues:
Could handle corners better i put in the comments what i think would work but if someone has a better idea lets work on it
