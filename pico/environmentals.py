import time
import dht
from csv import create_csv_file, write_data_to_csv
from datetime import get_timestamp
from machine import Pin, ADC, I2C
from ccs811 import CCS811
from pico_i2c_lcd import I2cLcd
from temp import c_to_f


#pir_pin = 28
#pir_sensor = Pin(pir_pin, Pin.IN)
headers = ["datetime", "temp", "humidity", "CO2", "tVOC"]
csv_filename = "environmentals.csv"

# LCD Setup
print("LCD_SETUP")
i2c_lcd = I2C(1, sda=Pin(2), scl=Pin(3), freq=100000)  # Reduced frequency for stability
lcd_addr = i2c_lcd.scan()
print(f"LCD Address: {lcd_addr}")
if not lcd_addr:
    raise Exception("LCD not found on I2C(1)")
lcd = I2cLcd(i2c_lcd, lcd_addr[0], 2, 16)
lcd.putstr("LCD Ready")

# Air Quality CCS811 Setup
i2c_air_sensor = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)  # Reduced frequency for stability
air_sensor_addr = i2c_air_sensor.scan()
print(f"Air Addr: {air_sensor_addr}")
if not air_sensor_addr:
    raise Exception("CCS811 not found on I2C(0)")
c = CCS811(i2c_air_sensor)
c.setup()

#DHT11 Setup
dht_pin = Pin(27)
dht_sensor = dht.DHT11(dht_pin)

i = 0
if create_csv_file(csv_filename, headers):
    while True:
        if c.data_available():
            try:
                dht_sensor.measure()
                temp_c = ("%3.1f" % dht_sensor.temperature())
                hum = ("%3.1f" % dht_sensor.humidity())
            except Exception as e:
                print(f"DHT11 Error: {e}")
                temp_c = 0
                hum = 0
            
            try:
                co2, tVOC = c.read_algorithm_results()
            except Exception as e:
                print(f"CCS811 Error: {e}")
                co2, tVOC = (0,0)
            
            temp_c = float(temp_c)
            
            # Only write to the file every 1 minute. 
            if i % 6 == 0:
                timestamp = get_timestamp()
                data = [timestamp, temp_c, hum, co2, tVOC]
                write_data_to_csv(csv_filename, [str(x) for x in data])
                
            lcd_temp = str(c_to_f(temp_c)).split(".")[0]
            lcd_hum = str(hum).split(".")[0]
            lcd.clear()
            lcd.putstr(f"T: {lcd_temp}f H: {lcd_hum}%\nC: {co2} tVOC: {tVOC}")
            time.sleep(10)
            lcd.clear()
            lcd.putstr("Re-Analyzing")

        
