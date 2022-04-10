import turtle
t1 = turtle.Turtle()

t1.penup
t1.goto(300,0)
t1.pendown
t1.write(t1.position())

t1.penup
t1.goto(300,300)
t1.pendown
t1.write(t1.position())

t1.penup
t1.goto(0,300)
t1.pendown
t1.write(t1.position())

t1.penup
t1.goto(0,0)
t1.pendown
t1.write(t1.position())
