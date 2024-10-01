# clock
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY
import time

# setup graphics
gu = GalacticUnicorn()
display = PicoGraphics(DISPLAY)


def cycle(iterable):
    # cycle('ABCD') → A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element

def updatescreen():
    display.set_pen(blackpen)
    display.clear()
    display.set_pen(pen)
    timetext = "{:02} : {:02} : {:02}".format(H, M, S)
    display.text(timetext, 2, 2, wordwrap = -1, scale = 1)
    gu.update(display)
    
def updateclock():
    global H, M, S
    S += 1
    S %= 60
    if S == 0:
        M += 1
        M %= 60
        if M == 0:
            H += 1
            H %= 24
            

COLOURS = ((255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255),(255,255,255))
colourcycle = cycle(COLOURS)

# set pen
r, g, b = next(colourcycle)
pen = display.create_pen(r, g, b)
blackpen = display.create_pen(0, 0, 0)
display.set_font('bitmap8')

H = 0
M = 0
S = 0            

running = False
a_released = b_released = c_released = True
currenttime = time.ticks_ms()
updatescreen()

while True:
    # What happens while running
    if running:
        # Update the time
        nexttime = time.ticks_ms()
        if  nexttime - currenttime >= 1000:
            currenttime = nexttime 
            updateclock()
            updatescreen()

        # Set the colour by pressing A
        if gu.is_pressed(GalacticUnicorn.SWITCH_A):
            if a_released:
                # Add code to change colour here
                print('Do something while running')
                r, g, b = next(colourcycle)
                pen = display.create_pen(r, g, b)
                a_released = False
                time.sleep(0.1)
        else:
            a_released = True

    # What happens before running
    else:
        # Set the hour by pressing A
        if gu.is_pressed(GalacticUnicorn.SWITCH_A):
            if a_released:
                H += 1
                H %= 24
                a_released = False
                updatescreen()
                time.sleep(0.1)
        else:
            a_released = True
            
        if gu.is_pressed(GalacticUnicorn.SWITCH_B):
            # Set the minute by pressing B
            if b_released:
                M += 1
                M %= 60
                b_released = False
                updatescreen()
                time.sleep(0.1)
        else:
            b_released = True
            
        if gu.is_pressed(GalacticUnicorn.SWITCH_C):
            # Allow the time to be set using a keyboard by pressing C
            if c_released:
                H, M, S = map(int, input('Enter starting time (HH:MM:SS): ').split(':'))
                c_released = False
                updatescreen()
                time.sleep(0.1)
        else:
            c_released = True
            
        if gu.is_pressed(GalacticUnicorn.SWITCH_D):
            # Start running by pressing D
            running = True
