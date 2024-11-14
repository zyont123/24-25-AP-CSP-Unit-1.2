# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

#-----game functions--------
def change_position(x,y):
    xpos = rand.randint(-150, 150)
    ypos = rand.randint(-175, 175)
    spot.goto(xpos, ypos)
    spot.goto()
    change_position()


Def update_score():
	Global score
    Score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)



#-----events----------------
Spot.onclick (spot_clicked)

wn = trtl.Screen()
wn.mainloop()

(#)Score

Score_writer = trtl.Turtle()
Score_writer.penup()
