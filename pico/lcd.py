from machine import Pin, ADC, I2C
from pico_i2c_lcd import I2cLcd
import time


print("LCD_SETUP")
i2c_lcd = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
I2C_ADDR = i2c_lcd.scan()[0]
print(I2C_ADDR)
lcd = I2cLcd(i2c_lcd, I2C_ADDR, 2, 16)
while True:
    lcd.blink_cursor_on()
    lcd.putstr("Test")
    time.sleep(2)
    lcd.clear()
    lcd.putstr("I2C Address:"+str(hex(I2C_ADDR))+"\n")
    lcd.putstr("Tom's Hardware")
    lcd.blink_cursor_off()
    lcd.clear()
    lcd.putstr("Backlight Test")
    for i in range(10):
        lcd.backlight_on()
        time.sleep(0.2)
        lcd.backlight_off()
        time.sleep(0.2)
    lcd.backlight_on()
    lcd.hide_cursor()
    for i in range(20):
        lcd.putstr(str(i))
        time.sleep(0.4)
        lcd.clear()
