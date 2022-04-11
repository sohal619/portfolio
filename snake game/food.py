from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(1, 1)
        self.speed("fastest")
        self.new_loc()

    def new_loc(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-240, 230)
        self.goto(random_x, random_y)
