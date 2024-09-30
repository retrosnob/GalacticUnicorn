# playing
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY
import time


# setup graphics
gu = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)
width = GalacticUnicorn.WIDTH
height = GalacticUnicorn.HEIGHT

# set pen
redpen = graphics.create_pen(255, 0, 0)
blackpen = graphics.create_pen(0, 0, 0)

w, h = graphics.get_bounds()

# set initial conditions
dx = dy = 1
x = y = 0

while True:
    print(x, y) # Just so we know it's running
    graphics.set_pen(blackpen)
    graphics.clear()
    graphics.set_pen(redpen)
    graphics.pixel(x, y)
    gu.update(graphics)
    time.sleep(0.05)
    x += dx
    y += dy
    if x == w - 1 or x == 0:
        dx = -dx
    if y == h - 1 or y == 0:
        dy = -dy

