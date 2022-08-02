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
    draw_circle(t, x + 60, y + 14, 3, 'silver', 'black')
    draw_scene(t, 1, "silver")
    
def draw_scene(t, scale, blade):
    draw_sword(t, 0, -120, 100, 30, 30, 90, 1, blade)


def draw_sword(t, x, y, height, width, side, tilt, scale, blade):
    """
    Draws a sword using the atomic shapes of rectangle, diamond, trapezoid 1 and 2, and circle.
    x, and y are for coordinates
    height is used for the hilts' rectangles
    Width is like the height
    tilt is used for the rectangles that are not facing the same direction.
    scale is used to determine the size of the sword, the parameter applies to all shapes herein.
    blade is for the blades color.
    """
    t.setheading(tilt)



    draw_diamond(t, x, (y + 280) * scale, side * scale, blade, 'black')
    draw_trapezoid(t, x * scale,(y + 280) * scale, side * scale, blade, 'black', scale)
    draw_trapezoid2(t, (x-30) * scale, (y + 280) * scale, side * scale, blade, 'black', scale)
    draw_rectangle(t, (x - 65) * scale, (y + 24) * scale, width * scale, height * scale, 0, '#7B3F00', 'black')
    draw_rectangle(t, (x + 35) * scale, (y + 24) * scale, (width -70) * scale, (height - 25) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(t, (x - 105) * scale, (y + 24) * scale, (width -70) * scale, (height - 25) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(t, (x - 30) * scale, (y + 14) * scale, (width -60) * scale, (height - 90) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(t, (x - 30) * scale, (y + 4) * scale, (width -60) * scale, (height - 90) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(t, (x - 30) * scale, (y - 6) * scale, (width -60) * scale, (height - 90) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(t, (x - 30) * scale, (y - 16) * scale, (width -60) * scale, (height - 90) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(t, (x - 30) * scale, (y - 26) * scale, (width -60) * scale, (height - 90) * scale, 90, '#7B3F00', 'black')
    draw_circle(t, (x - 15) * scale, (y - 66) * scale, 20 * scale, blade, 'black')










def draw_trapezoid(t, x, y, side, fillcolor, pencolor, scale):
    """
    Draws a side trapezoid (only used on the blade of the sword in coordination with trapezoid2)
    x, and y are for coordinates.
    side is for one of the sides.
    fillcolor is for the color inside of the shape
    pencolor is for the border of the shape
    scale is to allow for size adjustments
    """

    length1 = 200
    length2 = 16.2
    length3 = 226

    t.up()
    t.goto(x, y)
    t.setheading(240)
    t.down()
    t.color(pencolor, fillcolor)

    t.begin_fill()
    t.forward(side)
    t.left(30)
    t.forward(length1 * scale)
    t.left(90)
    t.forward(length2 * scale)
    t.left(90)
    t.forward(length3 * scale)
    t.end_fill()
    t.up()



#t, 0, -120, 30,  100,    30, 90)
#t, x, y, height, width, side, tilt
def draw_trapezoid2(t, x, y, side, fillcolor, pencolor, scale):
    """
    # Draws a side trapezoid (only used on the blade of the sword in coordination with draw_trapezoid)
    x, and y are for coordinates
    side is for one of the sides length. (Not the same as the other sides.)
    fillcolor is for the color inside of the shape
    pencolor is for the border of the shape
    scale is to allow for size adjustments
    """

    length1 = 200
    length2 = 16.2
    length3 = 226


    t.up()
    t.goto(x, y)
    t.setheading(300)
    t.down()
    t.color(pencolor, fillcolor)
    t.begin_fill()
    t.forward(side)
    t.right(30)
    t.forward(length1 * scale)
    t.right(90)
    t.forward(length2 * scale)
    t.right(90)
    t.forward(length3 * scale)
    t.end_fill()
    t.up()


#t, 0, -120, 30, 100, 30, 90)
#t, x, y, height, width, side, tilt
    
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
