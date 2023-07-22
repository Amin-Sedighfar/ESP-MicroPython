from machine import Pin, I2C
from sh1106 import SH1106_I2C
from ds1302 import DS1302
from time import sleep

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
oled = SH1106_I2C(128, 64, i2c, None, addr=0x3C)
ds = DS1302(Pin(14), Pin(12), Pin(13))  # CLK, DAT, RST

oled.sleep(False)
oled.invert(False)

def set_datetime():
     ds.date_time([2023, 7, 22, 5, 10, 40, 0, 0]) # set datetime.

# set_datetime()
    
while True:
    
    current = ds.date_time()
    formatted_date = "{:04d}/{:02d}/{:02d}".format(current[0], current[1], current[2])
    formatted_time = "{:02d}:{:02d}:{:02d}".format(current[4], current[5], current[6])
    
    oled.fill(0) 
    oled.rect(0,0,120,60,1)
    oled.text('Date:', 5, 3)
    oled.text(formatted_date, 8, 13)
    oled.hline(5,25,100,1)
    oled.text('Time:', 5, 30)
    oled.text(formatted_time, 8, 40)

    oled.show()
    sleep(1)

