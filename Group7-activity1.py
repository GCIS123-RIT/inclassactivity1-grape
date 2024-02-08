###
###
###
import turtle

t = turtle

def setPos(turta, x, y):
    turta.penup()
    turta.goto(turta, x, y)
    turta.pendown()

def hexagon(turta, hexa_color, border_color):
    """This function helps to draw hexagon with color and border color from 
    the user.
    hexa_color : This is the color of the hexagon  
    border_color : This is the color of hexagon border"""
    turta.pendown()
    turta.pencolor(border_color)
    turta.fillcolor(hexa_color)
    turta.begin_fill() 
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.end_fill()
    turta.penup()

def square(turta, square_color,border_color):
    turta.pendown()
    turta.pencolor(border_color)
    turta.fillcolor(square_color)
    turta.begin_fill()    
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.end_fill()
    turta.penup()

def circle(turta, circle_color,border_color):
    turta.pendown()
    turta.pencolor(border_color)
    turta.fillcolor(circle_color)
    turta.begin_fill()
    turta.circle(50)
    turta.end_fill()
    turta.penup()

    
