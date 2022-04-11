from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.x = 20
        self.snake_seg = []
        for _ in range(3):
            self.x -= 20
            snake = Turtle()
            snake.shape("square")
            snake.penup()
            snake.color("white")
            snake.setx(self.x)
            self.snake_seg.append(snake)
            self.boundary()

    def new_seg(self):
        snake = Turtle()
        snake.shape("square")
        snake.penup()
        self.snake_seg.append(snake)

    def right(self):
        if 0 <= self.snake_seg[0].heading() <= 90:
            if self.snake_seg[0].heading() != 0:
                self.snake_seg[0].right(90)
        elif 180 <= self.snake_seg[0].heading() <= 270:
            if self.snake_seg[0].heading() != 180:
                self.snake_seg[0].left(90)
        # mam method
        # if self.snake_seg[0].heading() != LEFT:
        #     self.snake_seg[0].setheading(RIGHT)

    def left(self):
        if 0 <= self.snake_seg[0].heading() <= 90:
            if self.snake_seg[0].heading() != 0:
                self.snake_seg[0].left(90)
        elif 180 <= self.snake_seg[0].heading() <= 270:
            if self.snake_seg[0].heading() != 180:
                self.snake_seg[0].right(90)
        # mam method
        # if self.snake_seg[0].heading() != RIGHT:
        #     self.snake_seg[0].setheading(LEFT)

    def down(self):
        if 0 <= self.snake_seg[0].heading() <= 90:
            if self.snake_seg[0].heading() != 90:
                self.snake_seg[0].right(90)
        elif 180 <= self.snake_seg[0].heading() <= 270:
            if self.snake_seg[0].heading() != 270:
                self.snake_seg[0].left(90)
        # mam method
        # if self.snake_seg[0].heading() != UP:
        #     self.snake_seg[0].setheading(DOWN)

    def up(self):
        if 0 <= self.snake_seg[0].heading() <= 90:
            if self.snake_seg[0].heading() != 90:
                self.snake_seg[0].left(90)
        elif 180 <= self.snake_seg[0].heading() <= 270:
            if self.snake_seg[0].heading() != 270:
                self.snake_seg[0].right(90)
        # mam method
        # if self.snake_seg[0].heading() != DOWN:
        #     self.snake_seg[0].setheading(UP)

    def movement(self):
        for segment in range(len(self.snake_seg) - 1, 0, -1):
            self.snake_seg[segment].color("white")
            new_x = self.snake_seg[segment - 1].xcor()
            new_y = self.snake_seg[segment - 1].ycor()
            self.snake_seg[segment].goto(new_x, new_y)
        self.snake_seg[0].forward(20)

    @staticmethod
    def boundary():
        boundary = Turtle()
        boundary.speed("fastest")
        boundary.hideturtle()
        boundary.goto(-285, 260)
        boundary.pensize(20)
        boundary.color("green")
        for _ in range(2):
            boundary.forward(565)
            boundary.right(90)
            boundary.forward(540)
            boundary.right(90)
