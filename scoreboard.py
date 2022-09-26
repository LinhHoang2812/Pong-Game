from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.score= 0
        self.write(f"{self.score}", False, align="center", font=("Arial", 50, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, align="center", font=("Arial", 50, "normal"))
