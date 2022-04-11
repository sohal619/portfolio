from turtle import Turtle
import random


class Cars:
    def __init__(self):
        self.colors = ["red", "green", "blue", "brown", "orange", "purple"]
        self.y = [-200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0,
                  200, 180, 160, 140, 120, 100, 80, 60, 40, 20]
        self.x = [-300, -280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0,
                  300, 280, 260, 240, 220, 200, 180, 160, 140, 120, 100, 80, 60, 40, 20]
        self.cars = []
        for _ in range(25):
            color = random.choice(self.colors)
            car = Turtle()
            car.penup()
            car.setheading(180)
            car.shape("square")
            car.color(color)
            self.cars.append(car)
            self.car_pos()

    def car_pos(self):
        for car in self.cars:
            x = random.choice(self.x)
            y = random.choice(self.y)
            car.goto(x, y)

    def movement(self, speed):
        for car in self.cars:
            y = random.choice(self.y)
            if car.xcor() < -300:
                car.goto(300, y)
            car.forward(speed)

    def car_crash(self, x):
        for car in self.cars:
            if car.distance(x) < 20:
                return 0
