# This is a code to check temp and humidity with DHT11 sensor

import dht

d = dht.DHT11(machine.Pin(2))

d.measure()
t = d.temperature()
h = d.humidity()

print(str(t))
print(str(h))
