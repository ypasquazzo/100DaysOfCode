import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from message import Message

screen = Screen()
screen.setup(width=800, height=500)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []
message = Message()

screen.listen()
screen.onkey(player.move, "Up")

count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count += 1

    if scoreboard.score < 4:
        if count % 5 == 0:
            cars.append(CarManager(scoreboard.score + 1))
    elif scoreboard.score < 8:
        if count % 4 == 0:
            cars.append(CarManager(scoreboard.score + 1))
    else:
        if count % 3 == 0:
            cars.append(CarManager(scoreboard.score + 1))

    for car in cars:
        car.move()

    if player.check_finish_line():
        player.reset_position()
        scoreboard.score += 1
        scoreboard.update_score()
        for car in cars:
            car.increase_speed()

    for car in cars:
        if player.distance(car.segments[0]) < 20 or player.distance(car.segments[1]) < 20:
            game_is_on = False
            message.game_over()
            break

screen.exitonclick()
