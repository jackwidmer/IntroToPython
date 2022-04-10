import random
import turtle

t1 = turtle.Turtle()
t1.pensize(5)
t1.screen.colormode(255)


while True:
    #t1.left(random.randint(0,360))
    #t1.forward(random.randint(0,400))
    x = random.randint(-300,300)
    y = random.randint(-200,200)
    t1.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t1.goto(x,y)
