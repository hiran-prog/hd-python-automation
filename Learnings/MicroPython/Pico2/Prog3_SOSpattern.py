# SOS pattern - Morse code

from machine import Pin # type: ignore
import time

led = Pin("LED", Pin.OUT)

def blink(duration):
    led.on()
    time.sleep(duration)
    led.off()
    time.sleep(0.1)

while True:
    # S = 3 short blinks
    for _ in range (3):
        blink(0.1)
    time.sleep(0.2)

    # O = 3 long blinks
    for _ in range (3):
        blink(0.4)
    time.sleep(0.2)

    # S = 3 short blinks
    for _ in range (3):
        blink(0.1)
    time.sleep(1)