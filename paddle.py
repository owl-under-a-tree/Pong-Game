from turtle import Turtle

class Paddle:  # Could have used inheritence 

    def __init__(self, POSITION):
        self.position = POSITION
        self.create_paddle()

    def create_paddle(self):
        self.paddle = Turtle(shape = "square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid= 5, stretch_len = 1)
        self.paddle.penup()
        self.paddle.goto(self.position)


    def move_up(self):
        self.paddle.sety(self.paddle.ycor() + 20)

    def move_down(self):
        self.paddle.sety(self.paddle.ycor() - 20)


