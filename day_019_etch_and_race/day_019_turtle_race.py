from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(1)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtles = {}
y = -125
for key in colors:
    turtles[key] = Turtle(shape='turtle')
    turtles[key].penup()
    turtles[key].color(key)
    turtles[key].goto(-230, y)
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for key in turtles:
        if turtles[key].xcor() > 230:
            winning_turtle = turtles[key].pencolor()
            if winning_turtle == user_bet:
                print("You won!")
            else:
                print(f"The winning turtle is {winning_turtle}. Better luck next time!")
            is_race_on = False
        random_distance = random.randint(0,10)
        turtles[key].forward(random_distance)

screen.exitonclick()