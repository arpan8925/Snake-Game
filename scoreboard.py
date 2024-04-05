from turtle import Turtle


POSITION_Y = 280
FONT = ("Roboto", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_point = 0
        self.highest_score = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(-20, POSITION_Y)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_point} & High Score: {self.highest_score}", False, font=FONT)

    def reset(self):
        if self.score_point > self.highest_score:
            self.highest_score = self.score_point
        self.score_point = 0
        self.update_scoreboard()

    def game_over(self):
        self.color("white")
        self.goto(-30, 0)
        self.write("GAME OVER", False, font=FONT)

    def increase(self):
        self.score_point += 1
        self.update_scoreboard()


