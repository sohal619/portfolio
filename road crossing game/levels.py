from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 240)
        self.level_updater(1)

    def level_updater(self, current_lvl):
        self.clear()
        self.write(f"LEVEL: {current_lvl}", False, "center", ("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Arial", 72, "normal"))
