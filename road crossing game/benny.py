from turtle import Turtle


class Benny(Turtle):
    def __init__(self):
        super().__init__()
        self.head = 0
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def up(self):
        self.head = 90
        self.movement()

    def down(self):
        self.head = 270
        self.movement()

    def left_(self):
        self.head = 180
        self.movement()

    def right_(self):
        self.head = 0
        self.movement()

    def movement(self):
        self.setheading(self.head)
        self.forward(20)
        self.setheading(90)
