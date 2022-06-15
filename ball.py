from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        x = self.xcor()
        y = self.ycor()
        if(x < 360 or y < 300):
            self.goto(x + 10, y + 10)