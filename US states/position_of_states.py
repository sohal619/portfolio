from turtle import Turtle


class Position(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def writer(self, x, y, w):
        self.goto(x, y)
        self.write(w)


