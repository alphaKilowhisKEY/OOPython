from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_from_score_file()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1    
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_to_score_file()
        self.score = 0
        self.update_scoreboard() 

    def read_from_score_file(self):
        with open("data.txt", mode="r") as file: 
            return int(file.read())    

    def save_to_score_file(self):   
        with open("data.txt", mode="w") as file: 
            file.write(f"{self.score}")      