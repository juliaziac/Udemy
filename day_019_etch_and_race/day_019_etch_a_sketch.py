from turtle import Turtle, Screen

arrow = Turtle()
screen = Screen()

def move_forward():
    arrow.forward(5)
    
def move_backward():
    arrow.back(5)
    
def counter_clockwise():
    arrow.left(3)
    
def clockwise():
    arrow.right(3)
    
def clear_screen():
    arrow.clear()
    


screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='a', fun=counter_clockwise)
screen.onkeypress(key='d', fun=clockwise)
screen.onkeypress(key='c', fun=clear_screen)
screen.exitonclick()