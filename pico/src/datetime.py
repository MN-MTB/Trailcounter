from machine import RTC
rtc = RTC()

def get_timestamp() -> str:
    timestamp = rtc.datetime()
    timestring="%04d-%02d-%02d %02d:%02d:%02d"%(timestamp[0:3] + timestamp[4:7])
    return timestring
