import turtle
t1 = turtle.Turtle()

distance = 100

while True:
    t1.forward(distance)
    t1.left(90) 
    distance = distance + 5
    if t1.xcor() >= 300:
        break
print("Maximum x-coordinate reached!")

