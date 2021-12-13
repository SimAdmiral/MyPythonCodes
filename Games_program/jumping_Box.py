import time
import turtle
import random
import sys
# misc

speed = 2.8
rang = 210
charspeed = 3
score = 0
# screen
win = turtle.Screen()

win.bgcolor("dark blue")
win.title("endless by jackhammer")
win.setup(600, 400)

# platform

plat = turtle.Turtle()

plat.color("grey")
plat.penup()
plat.shape("square")
plat.shapesize(9, 30)
plat.speed(0)
plat.goto(0, -100)

# charcter

char = turtle.Turtle()

char.color("black")
char.shape("square")
char.shapesize(1, 1)
char.speed(0)
char.hideturtle()
char.penup()
char.lt(180)
char.fd(280)
char.rt(90)
char.showturtle()
char.speed(charspeed)

# pen
pen = turtle.Turtle()

pen.color("yellow")
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(0, 150)
pen.write("PRESS SPACE BAR TO JUMP", align="center", font=("arial", 24, "bold"))

# definations
def Jump():
    char.fd(90)
    char.rt(90)
    char.fd(80)
    char.lt(90)
    char.backward(90)


# bindings
win.listen()
win.onkeypress(Jump, "space")

# game loop
while True:

    # speed of obstruction relative to score
    if score >= 3:
        speed = 3.6
        rang = 163

    if score >= 8:
        speed = 4.8
        rang = 123

    if score >= 15:
        speed = 5.8
        rang = 100

    if score >= 30:
        speed = 7.2
        rang = 82

    if score >= 50:
        speed = 8.4
        rang = 70

    if score >= 100:
        speed = 10
        rang = 59

    if score >= 20:
        speed = 20
        rang = 29

    # obstruction spawning

    do = True
    obc = turtle.Turtle()

    obc.goto(obc.xcor(), obc.ycor() + 10)
    obc.color("light blue")
    obc.shape("square")
    obc.shapesize(2, 1)
    obc.hideturtle()
    obc.speed(0)
    obc.penup()
    obc.fd(280)
    obc.showturtle()
    obc.rt(180)

    # collision detection
    for i in range(rang):
        if obc.xcor() == char.xcor() and obc.ycor() == char.ycor() or obc.xcor() > char.xcor() - 10 and obc.xcor() < char.xcor() + 10 and (
                obc.ycor() < char.ycor() + 20) and obc.ycor() > char.ycor() - 20:
            pen.undo()
            pen.write("Game Over Score Is " + str(score), align="center", font=("arial", 24, "bold"))
            time.sleep(3)
            turtle.bye()
        obc.fd(speed)

        # score
        if (obc.xcor() <= -290 and do == True):
            score += 1
            char.setpos(-280, 0)
            pen.undo()
            pen.write("Score: " + str(score), align="center", font=("arial", 24, "bold"))
            do = False
    obc.hideturtle()
turtle.mainloop()