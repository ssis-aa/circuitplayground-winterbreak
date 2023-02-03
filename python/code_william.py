# Write your code here :-)
import time
import audiobusio
from adafruit_circuitplayground import cp

def buttons():
    if cp.button_b:
        cp.play_tone(500, 0.1)
    if cp.button_a:
        cp.play_tone(100, 0.1)

def Fiyah():
    if cp.temperature >= 28:
        cp.pixels[2] = (255, 0, 0)
        cp.pixels[3] = (255, 0, 0)
        cp.pixels[6] = (255, 0, 0)
        cp.pixels[7] = (255, 0, 0)
        print("Temp:", cp.temperature)
        print((cp.temperature,))
        time.sleep(0.1)

    elif cp.temperature < 28:
        cp.pixels[2] = (0, 0, 255)
        cp.pixels[3] = (0, 0, 255)
        cp.pixels[6] = (0, 0, 255)
        cp.pixels[7] = (0, 0, 255)
        print("Temp:", cp.temperature)
        print((cp.temperature,))
        time.sleep(0.1)

def BRIGHT():
    if cp.light >= 50:
        cp.pixels[0] = (255, 255, 0)
        cp.pixels[1] = (255, 255, 0)
        cp.pixels[8] = (255, 255, 0)
        cp.pixels[9] = (255, 255, 0)
        print("Light:", cp.light)
        print((cp.light,))
        time.sleep(0.1)

    elif cp.light < 50:
        cp.pixels[0] = (0, 0, 0)
        cp.pixels[1] = (0, 0, 0)
        cp.pixels[8] = (0, 0, 0)
        cp.pixels[9] = (0, 0, 0)
        print("Light:", cp.light)
        print((cp.light,))
        time.sleep(0.1)

def MoVE():
    x, y, z = cp.acceleration
    if y < -0.5 or y > 0.5:
        cp.pixels[4] = (0, 255, 0)
        cp.pixels[5] = (0, 255, 0)
        print("Gyro:", y)
        print((y,))
        time.sleep(0.1)
    elif y > -0.5 or y < 0.5:
        cp.pixels[4] = (0, 0, 0)
        cp.pixels[5] = (0, 0, 0)
        print("Gyro:", y)
        print((y))
        time.sleep(0.1)

while True:
    buttons()
    BRIGHT()
    Fiyah()
    MoVE()
