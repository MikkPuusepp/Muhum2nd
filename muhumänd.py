import turtle
wn = turtle.Screen()        
wn.bgcolor("darkgreen")

L = turtle.Turtle()     
L.pensize(7)             
L.color("white")        

K = turtle.Turtle()
K.pensize(7)
K.color("white")

for m in mänd:
    L.forward(100)
    L.left(135)
    L.forward(80)
    L.right(90)
    L.forward(80)
    L.left(135)
    L.forward(100)
    L.right(90)
    


K.left(180)
K.forward(113)
K.right(90)
K.forward(113)
K.right(90)
K.forward(113)
K.right(90)
K.forward(113)

wn.exitonclick()
