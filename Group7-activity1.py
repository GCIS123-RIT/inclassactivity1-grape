import turtle

t = turtle

def setPos(turta, x, y):
    turta.penup()
    turta.goto(turtle, x, y)
    turta.pendown()

def hexagon(turta, hexa_color, border_color):
    
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



    
