# Ping Pong the game

import turtle
import winsound
win = turtle.Screen()
win.title("Ping Pong by Ninad")
win.bgcolor("Black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=4, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=4, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=('Courier', 20, "normal"))
# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_dwn():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_dwn():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Key Binds
win.listen()
win.onkeypress(paddle_a_up, 'w')
win.onkeypress(paddle_a_dwn, 's')
win.onkeypress(paddle_b_up, 'Up')
win.onkeypress(paddle_b_dwn, 'Down')
# Main Game
while True:
    win.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=('Courier', 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=('Courier', 20, "normal"))

    # Paddle Bounce
    if (ball.xcor() > 340 and ball.xcor() < 350) and ((ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40)):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and ((ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40)):
        ball.setx(-340)
        ball.dx *= -1

