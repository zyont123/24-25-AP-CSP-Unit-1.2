import turtle as trtl

# Set up the screen
wn = trtl.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

main_snake = trtl.Turtle()
main_snake.speed(0)
main_snake.shape("square")
main_snake.color("black")
main_snake.penup()
main_snake.goto(0, 0)
main_snake.direction = "stop"


wn = trtl.Screen()
wn.mainloop()