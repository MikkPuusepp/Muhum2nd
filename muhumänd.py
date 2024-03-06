import turtle
wn = turtle.Screen()        
wn.bgcolor("darkgreen")

Linda = turtle.Turtle()     
Linda.pensize(7)             
Linda.color("white")        

Kalev = turtle.Turtle()
Kalev.pensize(7)
Kalev.color("white")

for m in mänd:
    Linda.forward(100)
    Linda.left(135)
    Linda.forward(80)
    Linda.right(90)
    Linda.forward(80)
    Linda.left(135)
    Linda.forward(100)
    Linda.right(90)
    


Kalev.left(180)
Kalev.forward(113)
Kalev.right(90)
Kalev.forward(113)
Kalev.right(90)
Kalev.forward(113)
Kalev.right(90)
Kalev.forward(113)

wn.exitonclick()
