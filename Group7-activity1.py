import turtle

t = turtle

def setPos(turta, x, y):
    t.penup()
    t.goto(turtle, x, y)
    t.pendown()
    


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



    
