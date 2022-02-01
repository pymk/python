from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # turn off animation, but needs screen.update()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # ball speed
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()

    # detect collision with r_paddle
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 335
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -335
    ):
        ball.bounce_x()

    # r_paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # l_paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()
