from turtle import Turtle
Font=("Times New Roman", 18, "normal")
position="center"
class scoreboard(Turtle):
    Scores = 0
    def __init__(self):
        super().__init__()
        self.Scores = 0
        with open("High_score.txt") as file:
            self.high_score = int(file.read())
        # self.high_score = 0
        self.color("white")
        # self.clear()
        self.penup()
        self.goto(0,225)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.Scores} High Score: {self.high_score}", False,position, Font)


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False,"center", Font)
        self.clear()

    def reset(self):
        if self.high_score < self.Scores:
            self.high_score = self.Scores
            with open("High_score.txt","w") as file:
                file.write(f"{self.high_score}")

        self.Scores = 0
        self.update()

    def increase_score(self):
        self.Scores += 1
        self.update()





