from turtle import Turtle

SCORE_FONT = 'Courier', 20, 'normal'
GAME_OVER_FONT = 'Courier', 50, 'bold'
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f'Score: {self.l_score}', False, 'center', SCORE_FONT)
        self.goto(100, 200)
        self.write(f'Score: {self.r_score}', False, 'center', SCORE_FONT)
    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        self.sety(0)
        self.hideturtle()
        self.write('GAME OVER!', False, 'center', GAME_OVER_FONT)