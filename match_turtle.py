from turtle import Turtle
import tkinter as TK

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(3)
turtle.color("blue", "yellow")
turtle.penup()

while True:
    command = input(">").strip().split()
    # move 2 3 - ["move", "2", "3"]
    if command[0] in ("exit", "stop"):
        break
    if command[0] == "draw":
        # draw line 40
        shape = command[1]
        size = float(command[2])
        turtle.pendown()
        if shape == "line":
            turtle.forward(size)
        elif shape == "circle":
            turtle.circle(size)
