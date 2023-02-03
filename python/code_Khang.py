from adafruit_circuitplayground import cp
import time

import analogio
import simpleio
import board

cp.pixels.brightness = 0.3

RED = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
LIME = (127, 255, 0)
GREEN = (0, 255, 0)
TURQUOISE = (255, 127, 0)
LIGHT_BLUE = (0, 255, 255)
AZURE_BLUE = (0, 127, 255)
BLUE = (0, 0, 255)
VIOLET = (127, 0, 255)
OFF = (0, 0, 0)


PEAK_TEMP = 32

COLOR_CYCLE = [RED, ORANGE, YELLOW, LIME, GREEN, TURQUOISE, LIGHT_BLUE, AZURE_BLUE, BLUE, VIOLET]

TONE_CYCLE = [261.625565, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25, 587.33, 659.25]

# A & B Buttons + Neopixels + Loudspeaker
def color_wheel():
    if cp.button_a:

        for i in range(0, 10):
            print(i)
            cp.pixels[i] = COLOR_CYCLE[i]
            cp.play_tone(TONE_CYCLE[-i], 0.15)
            cp.pixels[i] = OFF
    if cp.button_b:

        for i in range(0, 10):
            cp.pixels[i] = COLOR_CYCLE[i]
            cp.play_tone(TONE_CYCLE[i], 0.15)
            cp.pixels[i] = OFF

# Microphone, thermometer

def temp_sound():
    temp = cp.temperature
    time.sleep(1)
    if temp >= PEAK_TEMP:
        cp.play_tone(260, 3)


# gyroscope,
def ACCEL():
    x, y, z = cp.acceleration
    #  print((x, y, z))
    time.sleep(0.1)
    if x > 3:
        cp.pixels[0:5] = GREEN * 5
        cp.pixels[5:10] = OFF * 5
    elif x < -3:
        cp.pixels[5:10] = RED * 5
        cp.pixels[0:5] = OFF * 5
    elif y > 3:
        cp.pixels[3:7] = GREEN * 4
    else:
        cp.pixels[0:10] = OFF * 10


# light sensor
def light_level_pixels():
    print("light:", cp.light)
    light_level = cp.light
    if light_level < 10:
        cp.pixels[0:10] = RED * 10
    elif light_level > 80:
        cp.pixels[0:10] = GREEN * 10

while True:
    color_wheel()
    ACCEL()
    temp_sound()
    light_level_pixels()




