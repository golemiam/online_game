# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import turtle

def game():
    # Use a breakpoint in the code line below to debug your script.
    t = turtle.Turtle()
    s = turtle.getscreen()


    draw_circle(t, 90, 40, 40, 360, 60, 20, "blue", "yellow")
    draw_circle(t, 270, -60, 40, 180, 40, 20, "red", "green")
    draw_rectangle(t, 25, -110, 90, 90, 90, "blue", "yellow")
    draw_diamond(t, 0, -110, 90, 120, "black", "silver")
    draw_triangle(t, -65, -120, 40, 0, "green", "red")

def draw_circle(t, tilt, x, y, ext, rad, step, pencolor, fillcolor):
    #Draws a circle, x, and y determine its start location, extent determines how much of the shape is drawn.
    t.setheading(tilt)
    t.up()
    t.goto(x, y)
    t.down()
    t.color(pencolor, fillcolor)
    t.begin_fill()
    t.circle(rad, extent=ext, steps=step)
    t.end_fill()
    t.up()

def draw_rectangle(t, x, y, height, width, tilt, pencolor, fillcolor):
    #Draws a basic Rectangle
    t.setheading(tilt)
    t.up()
    t.goto(x,y)
    t.down()
    t.color(pencolor, fillcolor)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.right(90) # This is to set the heading back to normal
    t.end_fill()
    t.up()

def draw_triangle(t, x, y, length, tilt, pencolor, fillcolor):
    #Draws an equilateral triangle
    t.setheading(tilt)
    t.up()
    t.goto(x,y)
    t.down()
    t.color(pencolor, fillcolor)
    t.begin_fill()
    for i in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()
    t.up()

def draw_diamond(t, x, y, length, tilt, pencolor, fillcolor):
    #Draws an equilateral triangle
    t.setheading(tilt)
    t.up()
    t.goto(x,y)
    t.down()
    t.color(pencolor, fillcolor)
    t.begin_fill()
    for i in range(2):
        t.forward(length)
        t.left(120)
        t.forward(length)
        t.left(60)
    t.end_fill()
    t.up()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
