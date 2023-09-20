Create a tennis game. You game simulate two tennis players in a pitch.
A tennis player is characterized by their name, their skill rate (which is a floating value between 0 and 1).
A tennis player can shoot a ball. 

When player A shoots a ball the speed of the ball is the product of their skill rate and a random value between 0 and 100 which represents the force applied to the ball by player A. Then player B should try to intercept the ball. The interception score is the product of their skill score and a random value between -1 and 5. If the resulting value is positive then they intercepted the ball else they didn't.

Whenever a player intercepts a ball, they immediately return it to the other player. and they get an increase of 1 in their score.

Whenever a player misses a ball they get a decrease of 1 in their score. and they return the ball to the other player.

The game ends whenever a player misses the ball 5 times.

When game ends, print the winner and their score.

To use random import the random library in python like this

Create a class name Ball()

import random