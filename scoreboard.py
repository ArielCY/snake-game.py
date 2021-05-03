from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 # initialize score to 0
        # self.high_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read()) # read only give you string, so we need to convert string to integer
        self.color("white")
        self.hideturtle() # arrow will disappear
        self.penup()
        self.goto(0, 270) # move scoreboard to the top
        self.update_scoreboard() # self.write(f"Score: {self.score}", False, align="center", font=("Arial", 24, "normal"))

    def update_scoreboard(self): # this function is created because it's used frequently
        self.clear()
        self.write(f"Score: {self.score} high Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score = self.score + 1
        # before incease score on scoreboard, we need to delete previous score, or the previous score and updated score will be overlapping.
        # self.clear() # clear previous text that is written
        self.update_scoreboard() # self.write(f"Score: {self.score}", False, align="center", font=("Arial", 24, "normal"))

    # def game_over(self):
    #     self.goto(0,0) # instead of going to default top(from __init__ setting), "Game Over" is going to show in the center(0, 0)
    #     self.write("Game Over !!", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data: # open with write mode, default is read mode
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
