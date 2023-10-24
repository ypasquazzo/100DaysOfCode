import json

from turtle import Screen

from paddle import Paddle
from ball import Ball
from brick import Brick
from message import Message

with open('game_settings.json', 'r') as file:
    settings = json.load(file)

screen_width = settings["SCREEN_WIDTH"]
screen_height = settings["SCREEN_HEIGHT"]
paddle_width = settings["PADDLE_WIDTH"]
paddle_height = settings["PADDLE_HEIGHT"]
ball_radius = settings["BALL_RADIUS"]
bricks_row = settings["BRICKS_ROW"]
bricks_col = settings["BRICKS_COL"]
bricks_width = settings["BRICK_WIDTH"]
bricks_height = settings["BRICK_HEIGHT"]

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle(-screen_height / 2 + 50)
ball = Ball()
message = Message()
message.update_score()

bricks = []
colors = ["purple", "red", "orange", "yellow", "white"]
for row in range(bricks_row):
    brick_row = []
    for col in range(bricks_col):
        brick = Brick(col, row, colors[row])
        brick_row.append(brick)
    bricks.append(brick_row)

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

while True:
    ball.move()
    screen.update()

    # Paddle collision
    if abs(paddle.ycor() - ball.ycor()) < paddle_height / 2 + ball_radius / 2 and \
            abs(paddle.xcor() - ball.xcor()) < paddle_width / 2 + ball_radius / 2:
        ball.dy *= -1
        print(f"Ball_Speed: {ball.ball_speed}")
        print(f"X_Speed: {ball.dx}")
        print(f"Y_Speed: {ball.dy}")
        print(abs(paddle.xcor() - ball.xcor()))
        # Add angle if collision close to the side of the paddle
        if abs(paddle.xcor() - ball.xcor()) > 40:
            ball.dx *= 1.25
        # Reduce angle if collision close to the side of the paddle
        if abs(paddle.xcor() - ball.xcor()) < 20:
            ball.dx /= 1.1

    # Bricks collision
    hit_row = None
    for row_num, brick_row in enumerate(bricks):
        for brick in brick_row:
            if abs(brick.ycor() - ball.ycor()) < bricks_height / 2 + ball_radius / 2 and \
                    abs(brick.xcor() - ball.xcor()) < bricks_width / 2 + ball_radius / 2:
                ball.dy *= -1
                brick.hideturtle()
                brick_row.remove(brick)
                message.score += 5 * (5-row_num)
                message.update_score()
                hit_row = row_num
                break  # Exit inner loop when a hit is detected
        if hit_row is not None:  # If a hit is detected, exit the outer loop
            break

    # Border collision
    if abs(ball.xcor() - screen_width / 2) < ball_radius or abs(ball.xcor() + screen_width / 2) < ball_radius / 2:
        ball.dx *= -1
    # Top wall collision
    if ball.ycor() > screen_height / 2 - ball_radius / 2:
        ball.dy *= -1
    # Bottom wall collision
    if ball.ycor() < -screen_height / 2 + ball_radius:
        message.game_over()
        break

    if all(not row for row in bricks):
        message.game_won()
        break

screen.exitonclick()
