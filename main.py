from re import L
from turtle import Screen, Turtle
from paddle import Paddle

right_paddle = Paddle(position=(350, 0))
left_paddle = Paddle(position=(-350, 0))

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
    screen.update()


screen.mainloop()