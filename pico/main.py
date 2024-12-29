import time
from csv import create_csv_file, write_data_to_csv
from datetime import get_timestamp
from machine import Pin

pir_pin = 28
pir_sensor = machine.Pin(pir_pin, machine.Pin.IN)
headers = ["datetime", "events_count"]
csv_filename = "motion_events.csv"

if create_csv_file(csv_filename, headers):
    while True:
        pir_state = pir_sensor.value()
        
        if pir_state == 1:
            timestamp = get_timestamp()
            write_data_to_csv(csv_filename, [timestamp, "1"])
            time.sleep(1)

        