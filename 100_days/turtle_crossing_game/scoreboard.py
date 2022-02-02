from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.user_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.user_score}", align="center", font=FONT)

    def add_score(self):
        self.user_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.user_score = 0
        self.update_scoreboard()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
