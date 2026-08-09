# First program - blink the onboard LED

from machine import Pin  # type: ignore
import time

led = Pin("LED", Pin.OUT)

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
