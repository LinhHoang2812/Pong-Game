from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard  import Scoreboard
import time

screen= Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

line = Turtle()
line.penup()
line.goto(0,300)
line.setheading(270)
line.color("white")
for _ in range(12):
    line.pendown()
    line.forward(50)
    line.penup()
    line.forward(50)

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))

ball= Ball()
score_r= Scoreboard((100,200))
score_l= Scoreboard((-100,200))

screen.listen()
screen.onkey(key= "Up",fun=paddle_r.up)
screen.onkey(key= "Down",fun=paddle_r.down)
screen.onkey(key= "w",fun=paddle_l.up)
screen.onkey(key= "s",fun=paddle_l.down)

time_stop=0.1

game_is_on= True
while game_is_on:
    time.sleep(time_stop)
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #dectect collision with right paddle
    if ball.xcor() >= 320 and ball.distance(paddle_r) < 50:
        ball.bounce_x()
        time_stop *= 0.9
    elif ball.xcor() <= -320 and ball.distance(paddle_l) < 50:
        ball.bounce_x()
        time_stop *= 0.9



    if ball.xcor() > 350:
        ball.reset_ball()
        score_l.add_score()
        time_stop = 0.1
    elif ball.xcor() < -350:
        ball.reset_ball()
        score_r.add_score()
        time_stop = 0.1


    screen.update()






screen.exitonclick()
