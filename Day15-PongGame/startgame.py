import turtle

screen=turtle.Screen()
screen.title("Pong game")
screen.bgcolor("white")
screen.setup(width=800 , height=600)
screen.tracer(0)

paddle_left=turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("black")
paddle_left.penup()
paddle_left.goto(-350,0)
paddle_left.shapesize(5,1)

paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.color("black")
paddle_right.shape("square")
paddle_left.penup()
paddle_right.goto(350,0)
paddle_right.shapesize(5,1)

ball=turtle.Turtle()
ball.speed(0)
ball.color("red")
ball.shape("circle")
ball.penup()
ball.dx=0.15
ball.dy=0.15

pen=turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.goto(0,250)
pen.write("Player A: 0  Player B: 0",align="center",font=("courier",20,"bold"))
pen.hideturtle()

score_a=0
score_b=0

def paddle_left_up():
    y=paddle_left.ycor()
    y+=20
    paddle_left.sety(y)

def paddle_left_down():
    y=paddle_left.ycor()
    y-=20
    paddle_left.sety(y)

def paddle_right_up():
    y=paddle_right.ycor()
    y+=20
    paddle_right.sety(y)

def paddle_right_down():
    y=paddle_right.ycor()
    y-=20
    paddle_right.sety(y)


screen.listen()
screen.onkeypress(paddle_left_up,"a")
screen.onkeypress(paddle_left_down,"z")
screen.onkeypress(paddle_right_up,"Up")
screen.onkeypress(paddle_right_down,"Down")

while True:
    screen.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.dx *=-1
        score_a += 1
        pen.clear()
        pen.write("Player A:{}  Player B: {} ".format(score_a,score_b) , align= "center" , font= ("courier",20,"bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{}  Player B: {} ".format(score_a, score_b), align="center", font=("courier", 20, "bold"))

    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < paddle_right.ycor()  +60 and ball.ycor() > paddle_right.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < paddle_left.ycor()  +60 and ball.ycor() > paddle_left.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1

