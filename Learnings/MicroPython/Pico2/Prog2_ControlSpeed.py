# Level 1 - Control Speed

from machine import Pin # type: ignore
import time 

led = Pin("LED", Pin.OUT)
delay = 0.2 # the value smaller = faster the blink

while True:
    led.on()
    time.sleep(delay)
    led.off()
    time.sleep(delay)