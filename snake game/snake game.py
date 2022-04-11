from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("~~SNAKE GAME~~")
screen.tracer(0)
screen.listen()

food = Food()
snake = Snake()
scoreboard = ScoreBoard()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

a = True
while a:
    screen.update()
    time.sleep(0.2)
    snake.movement()
    if snake.snake_seg[0].distance(food) < 20:
        scoreboard.score_updater()
        food.new_loc()
        snake.new_seg()
    if snake.snake_seg[0].xcor() < -276 or snake.snake_seg[0].xcor() > 265 or snake.snake_seg[0].ycor() < -260 \
            or snake.snake_seg[0].ycor() > 250:
        a = False
        scoreboard.game_over()
    for seg in snake.snake_seg[1:]:
        if snake.snake_seg[0].distance(seg) < 10:
            a = False
            scoreboard.game_over()
            scoreboard.high_score()


screen.exitonclick()
