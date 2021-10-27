#   a114_nested_loops_2.py 
import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()

y = -200
while (y < 200): 
  y = y + 50
  x = 300
  painter.goto(x,y)
  painter.color("red")
  painter.stamp()
  while (x < 0):
    x = x + 50
    painter.goto(x,y)
    painter.color("blue")
    painter.stamp()

wn = trtl.Screen()
wn.mainloop()