import network
from utime import sleep
import socket
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd

i2c = I2C(sda=Pin(4), scl=Pin(5), freq=400000) 
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

api_url = "http://YOUR_STATION_STATIC_IP_ADDRESS"
payload = ""
headers = "GET {} HTTP/1.1\r\nHost: {}\r\n\r\n".format(api_url, api_url.split("://")[1])

lcd.move_to(0,0)
lcd.putstr("Initialization")

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("SSID", "PASSWORD")
    sleep(4)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(3)
    lcd.move_to(0,0)
    lcd.putstr("Your IP Addr: ")
    lcd.move_to(0,1)
    lcd.putstr(wlan.ifconfig()[0])

def HttpRequest():
    s = socket.socket()
    s.connect((api_url.split("://")[1], 80))
    s.send(headers.encode())
    response = s.recv(1024)
    resp = str(response)
    temp = resp.index("Temperature")
    hum = resp.index("Humidity")
    lcd.move_to(0,0)
    lcd.putstr("Temperature: " + resp[temp+13:temp+15] + "C" )
    lcd.move_to(0,1)
    lcd.putstr("Humidity: " + resp[hum+10:hum+12] + "%")
    s.close()
        
connect()
while True:
    try:
        HttpRequest()
        sleep(10)
    except Exception as e:
        print("An error occurred:", e)
