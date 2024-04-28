from turtle import Turtle

FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1    
        self.clear()  
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)