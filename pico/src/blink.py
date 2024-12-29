from machine import Pin, Timer

led = Pin(25, Pin.OUT)
led_state = True
timer = Timer()

def tick(timer: Timer) -> None:
    global led_state, led
    led_state = not led_state
    led.value(led_state)
    #machine.lightsleep(1000)
    
timer.init(freq=1, mode=Timer.PERIODIC, callback=tick)
    
    