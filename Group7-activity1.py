'''
Ali Alblooshi-setPos, comments
Ameen Ahmed-Square and main()
Pranav Anil-Hexagon and Pattern
Mohammed Daaboul-Circle
'''

import turtle

def setPos(turta, x, y):
    '''This function sets the position of the turtle to the coordinates x and y without leaving any trace.'''
    turta.penup()
    turta.goto(x, y) 
    turta.pendown()
    turta.setheading(0)

def hexagon(turta, hexa_color, border_color):
    """This function helps to draw hexagon with color and border color from 
    the user.
    hexa_color : This is the color of the hexagon  
    border_color : This is the color of hexagon border"""
    turta.pendown()             
    turta.pencolor(border_color)
    turta.fillcolor(hexa_color) 
    turta.begin_fill()      #begins filling color
    turta.forward(50)       #moves forward
    turta.right(60)         #moves right
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.end_fill()        #stops filling color
    turta.penup()               

def square(turta, square_color,border_color):
    """This function helps to draw square with color and border color from 
    the user.
    square_color : This is the color of the square  
    border_color : This is the color of square border"""
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
    """This function helps to draw circle with color and border color from 
    the user.
    circle_color : This is the color of the circle  
    border_color : This is the color of circle border"""
    turta.pendown()
    turta.pencolor(border_color)
    turta.fillcolor(circle_color)
    turta.begin_fill()
    turta.circle(50)      # takes radius of circle to draw
    turta.end_fill()
    turta.penup()
    
def pattern(turta, hexa_color, circle_color, square_color, border_color):
    '''This function helps to draw all the shapes in a pattern that we desire.
    hexa_color : This is the color of the hexagon
    circle_color : This is the color of the circle
    square_color : This is the color of the square  
    border_color : This is the color of all the shape's borders'''
    setPos(turta, -250, 100 + 100)
    hexagon(turta, hexa_color, border_color)
    setPos(turta, -100,0 + 100)
    circle(turta, circle_color, border_color)
    setPos(turta, 0, 100+ 100)
    square(turta, square_color, border_color)
    
    setPos(turta, -250+100, -50+ 100)
    hexagon(turta, hexa_color, border_color)
    setPos(turta, -100+100, - 150 + 100)
    circle(turta, circle_color, border_color)
    setPos(turta, 0+100, -50+ 100)
    square(turta, square_color, border_color)
    
    setPos(turta, -250 + 200, -200+ 100)
    hexagon(turta, hexa_color, border_color)
    setPos(turta, -100+ 200, - 300 + 100)
    circle(turta, circle_color, border_color)
    setPos(turta, 0+ 200, -200+ 100)
    square(turta, square_color, border_color)
  
def main():
    turtle.bgcolor("sky blue")
    hexa_color = input("Enter the color of hexagon: ")
    circle_color = input("Enter the color of circle: ")
    square_color = input("Enter the color of square: ")
    border_color = input("Enter the color of shape borders: ")
    pattern(turtle, hexa_color, circle_color, square_color, border_color)
    
    input()
    
main()