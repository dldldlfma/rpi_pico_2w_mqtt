# rpi_pico_2w_mqtt

## Initialize

follow this document for initial setting
https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#what-is-micropython﻿

### Free MQTT Broker 

HiveMQ Cloud is the best option to fast test.

Check bellow link

https://www.hivemq.com/mqtt/public-mqtt-broker/



## install

In Thonny, Run this code for network connection
```
import time
import json
import network

# WiFi Info
ssid = "<YOUR_SSID>"
password = "<YOUR_PASSWORD>"


# WiFi Connect
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("Waiting for WiFi connection...")
    time.sleep(1)

print("WiFi connected:", wlan.ifconfig())
```


After that, In Thonny python ternimal, type bellow command for install umqtt.simple
```python
import mip
mip.install("umqtt.simple")
```

## run main.py in your rpi pico 2w 

