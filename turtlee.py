import turtle


lol = turtle.Screen()
lol.bgcolor("black")
lol = turtle.Turtle()
lol.pencolor("green")

a = 0
b = 0
lol.speed(45)
lol.penup()
lol.goto(0, 200)
lol.pendown()
while True:
    lol.forward(a)
    lol.right(b)
    a += 3
    b += 1
    if b == 180:
        break
    lol.hideturtle()

turtle.done()