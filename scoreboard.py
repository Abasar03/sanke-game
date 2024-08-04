from turtle import Turtle
ALIGNMENT="center"
FONT=("aerial",24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt",mode="r") as data:
            value=(data.read())
            if value == "":
                print("The file is empty. Setting high score to 0.")
                self.high_score = 0
            else:
                self.high_score = int(value)

        self.color("white")
        self.penup()
        self.goto(0,268)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High score:{self.high_score}", align=ALIGNMENT, font=FONT)


    def reset_score(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w")as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_score()

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
