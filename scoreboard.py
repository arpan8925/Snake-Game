from turtle import Turtle


POSITION_Y = 280
FONT = ("Roboto", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_point = 0
        self.score_text = f"Score: {self.score_point}"
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(-20, POSITION_Y)
        self.color("white")
        self.write(self.score_text, False, font=FONT)

    def game_over(self):
        self.color("white")
        self.goto(-30, 0)
        self.write("GAME OVER", False, font=FONT)

    def increase(self):
        self.score_point += 1
        self.score_text = f"Score: {self.score_point}"  
        self.clear() 
        self.write(self.score_text, False, font=FONT)


