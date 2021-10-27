#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle","classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple","gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  t.color(turtle_colors.pop())
  t.pencolor("black")
  my_turtles.append(t)

#  these are our starting coordinates. 
startx = 0
starty = 0
startDir = 90
forwardLength = 50
#loops through every turtle
for t in my_turtles:
  
  t.goto(startx, starty)
  t.pendown()
  t.setheading(startDir) 
  t.right(45)    
  t.forward(forwardLength)

#	the next turle will move more to the right and more up
  startx = t.xcor()
  starty = t.ycor()
  startDir  = t.heading()
  forwardLength += 3

wn = trtl.Screen()
wn.mainloop()