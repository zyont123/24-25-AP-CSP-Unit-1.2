import turtle as trtl
import random as rand

# intialize variables
wn = trtl.Screen()
maze_painter = (trtl.Turtle())
length = 35
path_width = 30


#setup turtle
maze_painter.left(90)
maze_painter.pensize(5)
maze_painter.speed(0)

# draw maze
# process
# draw line
# turn left
# increment length
# repeat
def draw_barrier(pos):
  maze_painter.forward(pos)
  maze_painter.left(90)
  maze_painter.forward(path_width)
  maze_painter.backward(path_width)
  maze_painter.right(90)

 # randomize location of doors and barriers in wall
door = rand.randint(path_width*2, (length - path_width*2))
barrier = rand.randint(path_width*2, ( length  - path_width*2))
 # if a door and barrier would be rendered on top of each other, get a new value
while abs(door - barrier) < path_width:
  door = rand.randint(path_width*2, (length- path_width*2))


for wall in range(21):
    maze_painter.forward(length/3)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    if wall > 5:
     draw_barrier(pow)
    maze_painter.forward(length- path_width - (length/3))
    maze_painter.left(90)
    length += 15








wn.listen()