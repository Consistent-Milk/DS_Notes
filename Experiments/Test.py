import turtle
import random
colors = ["red", "green", "blue", "yellow", "orange", "black", "purple"]
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle")
t = turtle.Turtle()

t.pendown()
for i in range(100):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    t.setposition(x, y)
    temp_color = random.randint(0, len(colors)-1)
    t.dot(colors[temp_color])
