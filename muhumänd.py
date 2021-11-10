import turtle
wn = turtle.Screen()        
wn.bgcolor("darkgreen")

Linda = turtle.Turtle()     # loo linda ja pliiatsi laius
Linda.pensize(7)             # muutuja nime muutmine -> Settings - Preferences - Editing - Multi-Editing Settings CTRL Key and click with the mouse the values
Linda.color("white")        # kommentaar käib notepad++ , programm kirjutatud 16.02.2021

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
