from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(1)
    s = Snake()
    s.move()

screen.exitonclick()   