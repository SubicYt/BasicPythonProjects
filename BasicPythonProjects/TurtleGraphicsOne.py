#   a114_nested_loops_4.py 
"""


Python Project made with turtle graphics.
It was an existing program that was modified to run infinitly, 
Thus why the user needs to input zero in order to put it
in an infinite loop. 

Comments are minimal, sorry about that
- Ethan Denning

"""
import turtle as trtl
painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()
x = -200
y = 0
move_x = 1
move_y = 1
num = int(input("enter 0"))
while(num>=0):
  while (x < 200):
    while (y < 100):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = -1
    while (y > 0):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = 1
  painter.penup()
  x = -200
  y=0
  painter.goto(x,y)
  painter.pendown()
  move_x = 1
  move_y = -1
  while (x < 200):
    while (y > -100):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = 1
    while (y < 0):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = -1
num = num+1
wn = trtl.Screen()
wn.mainloop()
