from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key = "Up", fun = right_paddle.move_up)
screen.onkey(key = "Down", fun = right_paddle.move_down)

screen.onkey(key="w",  fun= left_paddle.move_up)
screen.onkey(key="s", fun= left_paddle.move_down)




game_is_on = True


while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()


    #Detext collision with r and l paddle
    if ball.distance(right_paddle.paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle.paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    #Detect out of bounds case;

    if ball.xcor() < -380: # Detext L paddle misses
        ball.game_over()
        scoreboard.rpoint()

    if ball.xcor() > 380: # Detext R paddle misses
        ball.game_over()
        scoreboard.lpoint()



screen.exitonclick()
