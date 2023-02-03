# Write your code here :-)
import time
import analogio
from adafruit_circuitplayground.express import cpx
import neopixel
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1, auto_write=False)
pixels.fill((0,0,0))
pixels.show()

cpx.pixels.brightness = 0.1
cpx.pixels.fill((0, 0, 0))
cpx.pixels.show()

IDLE      = 0
PUMPING   = 1
PAUSED    = 2
AUTOMATIC = 3
DONE      = 4
OFF       = 5

currentState = IDLE

def Volume(int: volume):
    pass

def playSound():
    for i in range(4):
        cpx.play_tone(262, 1)

def buttonA():
    #global cpx.button_a
    cpx.button_a = True
    pass

def buttonB():
    #global cpx.button_b
    cpx.button_b = True
    pass

#(countdown) is inspired from the internet. Link to video : https://www.youtube.com/shorts/H_auoRDRgRs
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{02d}'.format
        print(timeformat, end='/r')
        time.sleep(1)
        time_sec -= 1
    print("stop")

def ACTIVATE_PUMP():
    print("MOTOR IS MOVING")

def Temperature_Celsius():
    cp.temperature

def updateSystem():
    global button_A_pressed
    global button_B_pressed


def evaluateState(state: int):
    global buttonA
    global buttonB

    if currentState == IDLE:
        if (buttonA):
            buttonA = False
            return PUMPING
        if (buttonB):
            buttonB = False
            return AUTOMATIC
        if (Temperature_Celsius) > 40:
            return PUMPING
    if currentState == PUMPING:
        if (buttonA):
            buttonA = False
            return DONE
        if (buttonB):
            buttonB = False
            return PAUSED
        if (timeformat) == [00,00]:
            return DONE
    if currentState == PAUSED:
        if (buttonA):
            return DONE
            buttonA = False
        if (buttonB):
            buttonB = False
            return PUMPING
    if currentState == AUTOMATIC:
        if (Timer) == (CALC_TIME):
            return PUMPING
        if (CircuitPlayground.lightSensor) > 1000:
            return PUMPING
    if currentState == DONE:
        if (buttonA):
            return IDLE
        if (buttonB):
            return PUMPING
    if currentState == OFF:
        if (buttonA):
            buttonA = False
            return IDLE
    return state


def reactToState(int: currentState):
    if currentState == IDLE:
        print("IDLE)")
        for j in range(4):
            pixels[0] = (0,0,0)
            pixels[1] = (0,0,0)
            pixels[2] = (0,0,0)
            pixels[3] = (0,0,0)
            pixels[4] = (0,0,0)
            pixels[5] = (0,0,0)
            pixels[6] = (0,0,0)
            pixels[7] = (0,0,0)
            pixels[8] = (0,0,0)
            pixels[9] = (0,0,0)
            time.sleep(0.5)
    if currentState == PUMPING:
        print("PUMPING")
        ACTIVATE_PUMP()
        for j in range(4):
            pixels[0] = (255,255,255)
            pixels[1] = (255,255,255)
            pixels[2] = (255,255,255)
            pixels[3] = (255,255,255)
            pixels[4] = (255,255,255)
            pixels[5] = (255,255,255)
            pixels[6] = (255,255,255)
            pixels[7] = (255,255,255)
            pixels[8] = (255,255,255)
            pixels[9] = (255,255,255)
            time.sleep(0.5)
    if currentState == PAUSED:
        pass

def on_forever():
    global currentState
    updateSystem()
    currentState = evaluateState(currentState)
    reactToState(currentState)

basic.forever(on_forever)
