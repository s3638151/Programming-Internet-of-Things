from sense_hat import SenseHat
import time

sense = SenseHat()

b = (0, 0, 255)
g = (0, 255, 0)
r = (255, 0, 0)

p = [
[
    g, g, g, g, g, g, g, g,

    g, g, g, g, g, g, g, g,

    g, b, b, g, g, b, b, g,

    g, b, b, g, g, b, b, g,

    g, g, g, b, b, g, g, g,

    g, g, b, b, b, b, g, g,

    g, r, r, r, r, r, g, g,

    g, g, b, g, g, b, g, g
],

[
    b, g, b, r, b, g, r, b,

    g, g, g, g, g, g, g, g,

    g, b, b, g, g, b, b, g,

    g, b, b, g, g, b, b, g,

    g, g, g, b, b, g, g, g,

    g, g, b, b, b, b, g, g,

    g, r, r, r, r, r, g, g,

    g, g, b, g, g, b, g, g
],

[
    b, g, b, r, b, g, r, b,

    g, g, g, g, g, g, g, g,

    g, b, b, g, g, b, b, g,

    g, b, b, g, g, b, b, g,

    b, g, b, r, b, g, r, b,

    g, g, b, b, b, b, g, g,

    g, r, r, r, r, r, g, g,

    g, g, b, g, g, b, g, g
]

]

while True:
    for i in range(3):
        sense.clear()
        sense.set_pixels(p[i])
        time.sleep(3)

