from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.current_score = 0
        self.write_score()

    def refresh_score(self):
        self.current_score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
