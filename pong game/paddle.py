from turtle import Turtle


class Paddle:
    def __init__(self):
        self.paddle = []
        self.y = -40
        self.head = 0
        for pad in range(4):
            self.y += 20
            pad_seg = Turtle()
            pad_seg.penup()
            pad_seg.speed("fastest")
            pad_seg.goto(-620, self.y)
            pad_seg.color("white")
            pad_seg.shape("square")
            self.paddle.append(pad_seg)

    def up(self):
        if self.paddle[3].distance(-620, 340) > 10:
            self.head = 90
            self.movement()

    def down(self):
        if self.paddle[3].distance(-620, -280) > 10:
            self.head = 270
            self.movement()

    def movement(self):
        for _ in self.paddle:
            _.setheading(self.head)
            _.forward(20)
