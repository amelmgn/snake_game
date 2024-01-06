from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color("black")
        self.refresh()

    def refresh(self):
        x_coord = randint(a=-280, b=280)
        y_coord = randint(a=-280, b=280)
        self.goto(x=x_coord, y=y_coord)
