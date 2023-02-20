from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.number = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.high_score = int(open('data.txt').read())

    def display(self):
        self.goto(0, 270)
        self.clear()
        self.write(f"Score: {self.number} High Score: {self.high_score}", False, align="center", font=("Times New Roman", 20, "normal"))

    def reset(self):
        with open("data.txt", mode="w") as score:

            if self.number > self.high_score:
                self.high_score = self.number
                score.write(f"{self.high_score}")
            self.number = 0
            self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=("Arial", 30, "normal"))

    def add_score(self):
        self.number += 1
