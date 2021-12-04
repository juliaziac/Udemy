from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
    
    
class Snake():
    
    def __init__(self):
        self.starting_positions = [(0,0), (-20,0), (-40,0)]
        self.segments = []
    
    for position in self.starting_positions:
        t = Turtle()
        t.color("white")
        t.shape("square")
        t.penup()
        t.setpos(position)
        self.segments.append(t)
    
    
    def __move__(self):
        game_is_on = True

        while game_is_on:
            screen.update()
            time.sleep(1)
            for seg_num in range(len(self.segments)-1, 0, -1):
                new_x = self.segments[seg_num-1].xcor()
                new_y = self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(20)
        
    