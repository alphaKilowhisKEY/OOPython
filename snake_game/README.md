# Snake Game

## Description
This Python script implements the classic Snake Game using the Turtle module for graphics. The game consists of a snake that moves around the screen eating food to grow longer. The player controls the snake's direction with arrow keys or keyboard controls.

## Features
- **Snake Movement**: The snake moves continuously in the direction set by the player.
- **Food Generation**: Food items randomly appear on the screen for the snake to eat, increasing its length and the player's score.
- **Score Tracking**: The game keeps track of the player's score and displays it on the screen.
- **Game Over**: The game ends when the snake collides with the wall or itself, displaying a game over message.

## Usage
1. Run the script to start the Snake Game: $python3 main.py
2. Control the snake's direction using the arrow keys (Up, Down, Left, Right) or keyboard controls (W, S, A, D).
3. Eat food items to increase your score and the length of the snake.
4. Avoid colliding with the walls or the snake's own body.
5. If the game ends, see your final score and try again.

## Requirements
- Python 3.x
- Turtle module

## Files
- **snake.py**: Defines the `Snake` class, which represents the snake in the game and controls its movement.
- **food.py**: Defines the `Food` class, which represents the food items that the snake eats to grow.
- **scoreboard.py**: Defines the `ScoreBoard` class, which manages the score tracking and display.
- **main.py**: The main script that initializes the game, sets up the screen, and controls the game flow.