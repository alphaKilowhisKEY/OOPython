# Cross the Road

## Description
This Python script implements a game where the player navigates a turtle across a busy road, avoiding oncoming cars. The player's goal is to reach the other side of the road without getting hit by any cars.

## Features
- **Player Movement**: The player can move the turtle upward using the up arrow key to cross the road.
- **Car Generation**: Cars randomly appear on the road, moving from right to left.
- **Level Up**: As the player successfully crosses the road, the level increases, and cars move faster.
- **Score Tracking**: The game keeps track of the player's level and displays it on the screen.
- **Game Over**: The game ends if the player collides with any car, displaying a game over message.

## Usage
1. Run the script to start the Cross the Road game.
2. Use the up arrow key to move the turtle upward and cross the road.
3. Avoid colliding with any cars moving on the road.
4. Reach the other side of the road to increase your level and score.
5. If the game ends, see your final level and try again.

## Requirements
- Python 3.x
- Turtle module

## Files
- **player.py**: Defines the `Player` class, representing the turtle controlled by the player.
- **car_manager.py**: Defines the `CarManager` class, managing the generation and movement of cars on the road.
- **scoreboard.py**: Defines the `Scoreboard` class, managing the score tracking and display.
- **main.py**: The main script that initializes the game, sets up the screen, and controls the game flow.