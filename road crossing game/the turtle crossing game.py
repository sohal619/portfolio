import time
from turtle import Screen
from benny import Benny
from cars import Cars
from levels import Level


screen = Screen()
screen.setup(600, 600)
screen.listen()
screen.tracer(0)

benny = Benny()
cars = Cars()
level = Level()

screen.onkey(key="Up", fun=benny.up)
screen.onkey(key="Down", fun=benny.down)
screen.onkey(key="Left", fun=benny.left_)
screen.onkey(key="Right", fun=benny.right_)

a = True
lvl = 1
while a:
    screen.update()
    time.sleep(0.1)
    cars.movement(lvl)
    if benny.ycor() > 260:
        lvl += 1
        level.level_updater(lvl)
        benny.goto(0, -280)

    if cars.car_crash(benny.pos()) == 0:
        a = False
        screen.clearscreen()
        level.game_over()

screen.exitonclick()
