from turtle import Turtle


class ComPaddle:
    def __init__(self):
        self.paddle2 = []
        self.y = -40
        self.h = 90
        for pad in range(4):
            self.y += 20
            pad_seg = Turtle()
            pad_seg.penup()
            pad_seg.speed("fastest")
            pad_seg.goto(620, self.y)
            pad_seg.color("white")
            pad_seg.shape("square")
            self.paddle2.append(pad_seg)

    def up_down(self):
        for _ in self.paddle2:
            _.setheading(self.h)
            _.forward(2)

    def movement(self):
        if self.paddle2[0].distance(620, 330) < 50:
            self.h = 270
        if self.paddle2[3].distance(620, -330) < 50:
            self.h = 90
        self.up_down()
