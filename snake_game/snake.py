""" 
This module provides functions to set up the screen 
and initialize a snake for the Snake Game.
"""

from turtle import Screen, Turtle
import time

SEGMENT_SIZE = 20
START_POSITIONS = [(0, 0), (-SEGMENT_SIZE, 0), (-2 * SEGMENT_SIZE, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        
    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)
          
    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)  

    def extend_snake(self):
        self.add_segment(self.snake[-1].position())        

    def move_snake(self):
        for seg in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE) 

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)   

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)   

    def reset(self): 
        for segment in snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()  
        self.head = self.snake[0]     