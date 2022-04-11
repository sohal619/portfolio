from turtle import Screen
from paddle import Paddle
from com_paddle import ComPaddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.listen()
screen.setup(1300, 700)
screen.title("😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁          P.O.N.G          😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁")
screen.tracer(0)

paddle = Paddle()
com_paddle = ComPaddle()
ball = Ball()
scoreboard = ScoreBoard()

screen.onkeypress(key="Up", fun=paddle.up)
screen.onkeypress(key="Down", fun=paddle.down)

score = 0
score2 = 0
a = True
while a:
    screen.update()
    com_paddle.movement()
    if ball.ycor() > 335 or ball.ycor() < -330:
        ball.wall_detector()
    ball.movement()
    for _ in range(4):
        if paddle.paddle[_].distance(ball) < 25:
            ball.ball_bouncer()
        if com_paddle.paddle2[_].distance(ball) < 28:
            ball.ball_bouncer2()
    if ball.xcor() < -630 or ball.xcor() > 630:
        if ball.xcor() < -630:
            score2 += 1
            scoreboard.score_updater(score, score2)
        elif ball.xcor() > 630:
            score += 1
            scoreboard.score_updater(score, score2)
        ball.new_ball()
        screen.update()
        time.sleep(1)
    if score == 5 or score2 == 5:
        screen.clearscreen()
        a = False
        scoreboard.result(score, score2)
        screen.update()

screen.exitonclick()
