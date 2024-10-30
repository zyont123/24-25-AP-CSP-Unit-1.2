# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

#-----game functions--------
def change_position(x,y):
    xpos = rand.randint(1, 400)
    ypos = rand.randint(1, 300)
    spot.goto(xpos, ypos)
def spot_click(x, y):
        spot.goto(x, y)
        change_position(x, y)


#-----events----------------
wn = trtl.Screen()
wn.mainloop()