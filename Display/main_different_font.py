# More details can be found in TechToTinker.blogspot.com 
# George Bantique | tech.to.tinker@gmail.com

from machine import Pin, I2C
from sh1106 import SH1106_I2C
import freesans20
from writer_minimal import Writer

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000) 
oled = SH1106_I2C(128,64,i2c,None,addr=0x3C)

# # create a writer instance
font_writer = Writer(oled, freesans20)
# # # set writing position
# font_writer.set_textpos(4, 40)
# # # write some text!
# font_writer.printstring("Hello")
# oled.text("Don't Forget to", 4, 30)
# oled.text("Subscribe my", 4, 40)
# oled.text("YouTube Channel", 4, 50)
# 
font_writer.set_textpos(4, 20)
font_writer.printstring("YouTube")
font_writer.set_textpos(20, 40)
font_writer.printstring("Amin")
font_writer.set_textpos(40, 20)
font_writer.printstring("Sedighfar")

oled.show()
oled.invert(True)

