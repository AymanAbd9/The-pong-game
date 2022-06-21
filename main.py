from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from time import sleep
from scoreboard import Scoreboard


right_paddle = Paddle(position=(350, 0))
left_paddle = Paddle(position=(-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


def move_up():
    x = right_paddle.xcor()
    y = right_paddle.ycor() + 20
    right_paddle.goto(x , y)

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if(ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
        ball.move_speed *= 0.85

    # Detect if the ball if the right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_point()


    # Detect if the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_point()


    


screen.mainloop()