from turtle import Screen
from paddle import Paddle
from ball import Ball
from message import Message

SCREEN_W = 800
SCREEN_H = 600

screen = Screen()
screen.setup(width=SCREEN_W, height=SCREEN_H)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(375)
l_paddle = Paddle(-375)
ball = Ball()
message = Message()

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

while True:
    ball.move()
    screen.update()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_wall()

    if r_paddle.xcor() - ball.xcor() < 20 and ball.distance(r_paddle) < 50 \
            or ball.xcor() - l_paddle.xcor() < 20 and ball.distance(l_paddle) < 50:
        ball.bounce_paddle()

    if ball.xcor() <= -400:
        message.game_over("Right")
        break
    if ball.xcor() >= 400:
        message.game_over("Left")
        break

screen.exitonclick()
