from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car_chance = random.randint(1, 50)
        if car_chance == 1:
            car = Turtle(shape="square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            color = random.choice(COLORS)
            car.color(color)
            ran_y = random.randint(-240, 240)
            car.penup()
            car.goto(300, ran_y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT