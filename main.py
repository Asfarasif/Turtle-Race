import random
import time
from car_manager import CarManager
from player import Player
from turtle import Screen
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(player.go_up,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if (random.randint(1,6) == 5):
        car_manager.create_cars()
    car_manager.move_cars()



    for cars in car_manager.all_cars:
        if cars.distance(player) < 30:
            game_is_on = False
            score.game_over()

    if player.reach_finish_line():
        player.goto_start()
        car_manager.level_up()
        score.increase_level()




screen.exitonclick()
