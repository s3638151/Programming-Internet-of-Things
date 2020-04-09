from sense_hat import SenseHat
import time
import json

with open("config.json") as f:
    setting = json.loads(f.read())

print(setting)
sense = SenseHat()

blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

while True:
    sense.clear()
    temp = sense.get_temperature()
    print(temp)
    temp = round(temp, 2)
    if temp < setting["cold_max"]:
        sense.show_message(str(temp), text_colour=blue)
    elif temp < setting["comfortable_max"]:
        sense.show_message(str(temp), text_colour=green)
    elif temp >= setting["hot_min"]:
        sense.show_message(str(temp), text_colour=red)
    time.sleep(10)

