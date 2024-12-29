from machine import Pin
import time

led = Pin(25, Pin.OUT)

def blink(n: int) -> None:
    for _ in range(n):
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)

    
    