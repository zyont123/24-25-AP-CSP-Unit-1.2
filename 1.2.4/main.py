import turtle as trtl

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
def draw_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)

for wall in range(20):
    maze_painter.forward(length/3)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    if(wall > 5):
     draw_barrier()
    maze_painter.forward(length- path_width - (length/3))
    maze_painter.left(90)
    length += 15









wn.listen()