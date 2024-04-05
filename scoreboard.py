from turtle import Turtle


POSITION_Y = 280
FONT = ("Roboto", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_point = 0
        self.read_score()
        self.highest_score = self.def_score
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(-20, POSITION_Y)
        self.color("white")
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_point} & High Score: {self.def_score}", False, font=FONT)

    def reset(self):
        if self.score_point > self.def_score:
            self.def_score = self.score_point
            self.write_score()
        self.score_point = 0
        self.update_scoreboard()


    def game_over(self):
        self.color("white")
        self.goto(-30, 0)
        self.write("GAME OVER", False, font=FONT)

    def read_score(self):
        with open("data.txt", mode="r") as file:
            self.def_score = int(file.read())

    def write_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.score_point))

    def increase(self):
        self.score_point += 1
        self.update_scoreboard()


