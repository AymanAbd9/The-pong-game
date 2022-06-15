from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from time import sleep


right_paddle = Paddle(position=(350, 0))
left_paddle = Paddle(position=(-350, 0))
ball = Ball()

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
    sleep(00000.1)
    screen.update()
    ball.move()
    if(ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce()
    


screen.mainloop()