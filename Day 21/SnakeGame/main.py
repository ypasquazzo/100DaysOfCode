from scoreboard import ScoreBoard
from food import Food
from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake_speed = screen.numinput(title="Difficulty", prompt="Choose your difficulty mode (1/2/3)",
                              default=2, minval=1, maxval=3)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

while True:
    screen.update()
    time.sleep(0.3/snake_speed)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
            or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        break

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.game_over()
            break

screen.exitonclick()
