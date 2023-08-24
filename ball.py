from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.move_speed = 0.01
        self.x_move = 3
        self.y_move = 3

    def create_ball(self):
        self.penup()
        self.color('white')
        self.shape('circle')

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        self.bounce_x()








