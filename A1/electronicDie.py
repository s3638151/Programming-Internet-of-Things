from sense_hat import SenseHat
import random
import time

sense = SenseHat()
class Dice:


    def check_shake(self): # this will block until a shake is detect

        old = sense.get_accelerometer_raw()
        print("wait to shake")
        while True:
            time.sleep(0.3)
            acc = sense.get_accelerometer_raw()
            x1, y1, z1 = round(old['x'], 0), round(old['y'], 0), round(old['z'], 0)
            x2, y2, z2 = round(acc['x'], 0), round(acc['y'], 0), round(acc['z'], 0) 
            if abs(x1-x2) + abs(y1-y2)+abs(z1-z2) >= 2:
                return random.randint(1, 6)


if __name__=="__main__":
    dice = Dice()
    while True:
        n = dice.check_shake()
        for i in range(3):
            sense.show_message(str(n))
        time.sleep(1)
