from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = random.randint(1,4)
        self.y_move = random.randint(1,4)
        self.increase_speed()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.increase_speed()

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()


    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.x_move=2
        self.y_move=2

    def increase_speed(self):
        self.y_move*=1.08 #increases the speed of the ball when it collides with the pads 
        self.x_move*=1.08
