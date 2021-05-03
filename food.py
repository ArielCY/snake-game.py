from turtle import Turtle
import random

class Food(Turtle): # Food inherit from Turtle class, superclass is Turtle

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # 20 pixel -> 10 pixel, 10/20 = 0.5
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self): # food go to new random position
        rand_x = random.randint(-280, 280)  # screen range (-300, 300), exclude edge (20)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)