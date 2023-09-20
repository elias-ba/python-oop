# Tennis Game Simulation Exercise

## Objective

Develop a program that simulates a tennis game between two players. Use object-oriented principles to model the players and the ball they play with. Your simulation should consider the players' skills, the unpredictability of the game, and the speed of the ball.

## Instructions

### Setup

Create a class named Ball to represent the tennis ball.
Create a class named Player to represent a tennis player.

#### Player Class

- Attributes:
  - name: Represents the player's name.
  - skill_rate: A floating-point number between 0 and 1, indicating the skill level of the player. A higher number indicates a more skilled player.
- Methods:

  - shoot_ball(): Simulate the player shooting the ball. The speed of the ball should be a product of the player's skill_rate and a random number between 0 and 100.

  - intercept_ball(ball_speed): Determine whether the player successfully intercepts a ball, considering its speed. The likelihood of intercepting the ball should be influenced by the player's skill_rate, the speed of the incoming ball, and some randomness. Use the formula `intercept_chance = skill_rate * random.uniform(0.5, 1.5) - ball_speed * 0.01`. If intercept_chance is positive, the player intercepts the ball; otherwise, they miss it.

#### Ball Class

- Attributes:
  - speed: The speed of the ball when it's shot or returned by a player.

### Game Logic

Start with two players. You can decide their names and skill rates.
Player A begins by shooting the ball to Player B.
Player B tries to intercept the ball using the method described above.
If Player B intercepts the ball, they return it, and their score increases by one. If they miss, their score decreases by one, and Player A gets another turn to shoot.
Players continue taking turns until one of them misses the ball five times.
Display the player with the higher score as the winner.

- Extras: Implement a game loop so multiple rounds can be played.
  Enhance the game's logic, such as adding special shots or introducing stamina for players, which might decrease as the game progresses.

### Notes

You'll need to use the random module in Python for generating random numbers.
The speed of the ball and the skill of the players should play a pivotal role in the dynamics of the game.
The formula for ball interception takes into account both the skill of the player and the speed of the ball, introducing a blend of predictability and unpredictability.

## Evaluation

You will be evaluated based on:

1. Your use of object-oriented principles.
2. The clarity and readability of your code.
3. Your ability to simulate the dynamics of a tennis game realistically.
