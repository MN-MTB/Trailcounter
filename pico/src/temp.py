from machine import ADC

#onboard sensor
adc_pin = 4
temp_sensor = ADC(adc_pin)

def get_cpu_temp_c() -> float:
    adc_value = temp_sensor.read_u16()
    volt = (3.3/65535)*adc_value
    temp = 27 - (volt - 0.706)/0.001721
    return round(temp, 1)

def get_cpu_temp_f() -> float:
    c = get_temp_c()
    return c_to_f(c)

def c_to_f(temp_c: float) -> float: 
    temp_f = temp_c * (9/5) + 32 
    return temp_f