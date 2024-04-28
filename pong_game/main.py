from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(right_paddle.go_up, "Up")  
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")  
screen.onkey(left_paddle.go_down, "s") 

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detecting collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detecting collision with a paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() > -320: 
        ball.bounce_x() 

    #Detecting if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()   
        scoreboard.l_point() 

    #Detecting if left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()  
        scoreboard.r_point()    

screen.exitonclick()