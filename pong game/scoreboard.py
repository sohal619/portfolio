from turtle import Turtle


class ScoreBoard:
    def __init__(self):
        self.board = []
        a = -60
        for _ in range(3):
            num = Turtle()
            num.goto(a, 245)
            num.hideturtle()
            num.color("white")
            self.board.append(num)
            a = 60
        self.score_screen(0, 0)

    def score_screen(self, s, s2):
        self.board[0].write(f"{s}", False, "center", ("Terminal", 80, "normal"))
        self.board[1].write(f"{s2}", False, "center", ("Terminal", 80, "normal"))

    def score_updater(self, score, score2):
        self.board[0].clear()
        self.board[1].clear()
        self.score_screen(score, score2)

    def result(self, s, s2):
        self.board[2].goto(0, 0)
        self.board[2].color("black")
        self.board[2].hideturtle()
        if s == 5:
            self.board[2].write("You Win!!", False, "center", ("Terminal", 100, "normal"))
        elif s2 == 5:
            self.board[2].write("You Lose", False, "center", ("Terminal", 100, "normal"))
        self.board[2].hideturtle()
