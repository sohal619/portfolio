import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.r_angel = 0
        self.angels = [0, 15, 25, 35, 45]
        self.goto(0, 350)
        self.color("white")
        self.pensize(5)
        self.shape("circle")
        self.shapesize(1.5)
        self.setheading(270)
        for a in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.setheading(180)
        self.color("red")
        self.goto(0, 0)
        self.new_ball()

    def new_ball(self):
        self.goto(0, 0)
        self.setheading(180)
        self.r_angel = random.choice(self.angels)
        self.right(self.r_angel)

    def wall_detector(self):
        n_angel = -self.r_angel
        self.right(n_angel)

    def ball_bouncer(self):
        self.setheading(0)
        self.r_angel = random.choice(self.angels)
        self.right(self.r_angel)

    def ball_bouncer2(self):
        self.setheading(180)
        self.r_angel = random.choice(self.angels)
        self.right(self.r_angel)

    def movement(self):
        self.forward(2)
