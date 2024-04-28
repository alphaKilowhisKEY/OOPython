# Pong Game

## Description
This Python script implements the classic Pong game using the Turtle module. It features two paddles controlled by the players and a ball that bounces off the walls and paddles. The game keeps track of the score and displays it on the screen.

## Features
- **Paddle Control**: Players can control the paddles using the arrow keys (for the right paddle) and the "W" and "S" keys (for the left paddle).
- **Ball Movement**: The ball moves continuously and bounces off the walls and paddles.
- **Score Tracking**: The game keeps track of the score for both players and displays it on the screen.
- **Game Over Detection**: The game ends when one player misses the ball, and the score is updated accordingly.

## Usage
1. Run the script to start the game: $python3 main.py
2. Use the arrow keys (up and down) to control the right paddle and the "W" and "S" keys to control the left paddle.
3. Try to prevent the ball from hitting the walls behind your paddle.
4. Score points by making the ball pass your opponent's paddle.
5. The game ends when one player reaches the maximum score.

## Requirements
- Python 3.x
- Turtle module (should be included in Python standard library)

## Files
- **ball.py**: Defines the `Ball` class, which represents the game ball.
- **paddle.py**: Defines the `Paddle` class, which represents the paddles controlled by the players.
- **scoreboard.py**: Defines the `Scoreboard` class, which tracks and displays the score.
- **main.py**: The main script that initializes the game, sets up the screen, and controls the game flow.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits
This project was created by [Your Name].
