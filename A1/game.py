from electronicDie import Dice
from datetime import datetime
from sense_hat import SenseHat
import time

sense = SenseHat()


class Player:

    def __init__(self, dice, color):
        self.dice = dice
        self.score = 0
        self.color = color
    
    def shake(self):
        sense.show_message("ready", text_colour=self.color)
        n = self.dice.check_shake()
        self.score += n
        for i in range(2):
            sense.show_message(str(n), text_colour=self.color)
        return n
    
    def isWin(self):
        if self.score > 30:
            sense.show_message("My score is:"+str(self.score)+" I win!", text_colour=self.color )
        return self.score > 30

class Game:
    
    def __init__(self):
        dice = Dice()
        self.p1 = Player(dice, (0, 0, 255))
        self.p2 = Player(dice, (255, 0, 0))
        self.winner = ""
        sense.show_message("player1 will use this color", text_colour=(0, 0, 255))
        time.sleep(1)
        sense.show_message("player2 will use this color", text_colour=(255, 0, 0))
    
    def run(self):
        while True:
            self.p1.shake()
            time.sleep(1)
            if self.p1.isWin():
                self.winner = "player1"
                break
            
            self.p2.shake()
            time.sleep(1)
            if self.p2.isWin():
                self.winner = "player2"
                break
        self.output()

    def output():
        with open("winner.csv", "a+") as f:
            f.write(str(datetime.now()), str(max(self.p1.score, self.p2.score)))
        

if __name__ == "__main__":
    Game().run()
