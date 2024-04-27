from turtle import Turtle, Screen
import time
import random



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_change = 10
        self.y_change = 10
        # self.goto(0, -260)
    def move(self):
        new_x = self.xcor() + self.x_change
        new_y = self.ycor() + self.y_change
        self.goto(new_x, new_y)
    def bounce(self):
        #change in y direction
        self.y_change *= -1
    def paddle_bounce(self):
        #change in x direction.
        self.x_change *= -1





def line():
    # middle line
    middle_line = Turtle()
    middle_line.hideturtle()
    middle_line.color("white")
    middle_line.penup()
    middle_line.goto(x=0, y=300)
    middle_line.setheading(270)
    for _ in range(60):
        middle_line.pendown()
        middle_line.forward(5)
        middle_line.penup()
        middle_line.forward(5)
        middle_line.pendown()






class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.paddle = []
        self.create()
        self.paddle[0].goto(position)
    def create(self):
        for _ in range(2):
            self.shape("square")
            self.color("white")
            self.penup()
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.paddle.append(self)


    def up(self):
        y = self.paddle[0].ycor() + 30
        self.paddle[0].goto(self.paddle[0].xcor(),y)

    def down(self):
        y = self.paddle[0].ycor() - 30
        self.paddle[0].goto(self.paddle[0].xcor(), y)


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score =0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(position)
        self.s_write()
    def s_write(self):
        self.write(f"{self.score}", align="center", font=("Courier", 22, "normal"))
    def update_score(self):
        self.clear()
        self.score += 1
        self.s_write()
    def gameover(self):
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 0)
        self.write("GameOver", align="center", font=("Courier", 12, "normal"))




screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
ball = Ball()
line()
l_paddle = Paddle((-380,0))
r_paddle = Paddle((380,0))
score2 = Score((100,270))
score1 = Score((-100,270))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "x")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    #detect the colllision with top_bottom all.
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounnce
        ball.bounce()

    #detect collision with side wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        score1.gameover()
        game_is_on = False



    #detect collision with right-paddle
    if r_paddle.distance(ball) <50 and ball.xcor() >350:
        score2.update_score()
        ball.paddle_bounce()
    #detect collision with left-paddle
    if l_paddle.distance(ball) < 50 and ball.xcor() < -350:
        score1.update_score()
        ball.paddle_bounce()




screen.exitonclick()