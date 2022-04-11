from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.h_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("red")
        self.score_screen()
        self.high_score()

    def score_screen(self):
        self.goto(-210, 267)
        self.write(f"Score :  {self.score}", False, "center", ("Arial", 24, "normal"))

    def high_score(self):
        self.goto(150, 267)
        if self.h_score < self.score:
            self.h_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.h_score))
        self.write(f"HIGH Score :  {self.h_score}", False, "center", ("Arial", 24, "normal"))

    def score_updater(self):
        self.score += 1
        self.clear()
        self.score_screen()
        self.high_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Arial", 30, "normal"))
