from turtle import Turtle, Screen
from ball import Ball
from score import Score
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Ping Pong')
screen.bgcolor('black')
screen.tracer(0)

paddle_R = Paddle((350, 0))
paddle_L = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.onkey(paddle_R.up, 'Up')
screen.onkey(paddle_R.down, 'Down')
screen.onkey(paddle_L.up, 'w')
screen.onkey(paddle_L.down, 's')
screen.listen()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # collide with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with paddle
    if ball.distance(paddle_R) < 50 and ball.xcor() > 320 or ball.distance(paddle_L) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
