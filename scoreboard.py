from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Helvetica', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.print_score()

    def print_score(self, score=0):
        self.refresh()
        self.write(f"Score = {score} ", align=ALIGNMENT, font=FONT)

    def game_is_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.goto(-0, 280)
