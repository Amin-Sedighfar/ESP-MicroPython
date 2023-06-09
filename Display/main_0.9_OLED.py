from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 
# i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello, World 1!', 0, 0)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)
oled.text('Hello, World 4!', 0, 30)
oled.text('Hello, World 5!', 0, 40)
oled.text('Hello, World 6!', 0, 50)
oled.show()

# sample commands
# oled.fill(1)
# oled.fill(0)
# oled.pixel(0, 0, 1)
# oled.invert(True)
# oled.invert(False)
