####################################################
#                Hello RPI PICO 2w                 #
#       Example of PRI PICO 2w MQTT using WiFi     #
####################################################

import time
import json
import network
import random
from machine import Pin
from umqtt.simple import MQTTClient


led = Pin("LED", Pin.OUT)

ssid = <WIFI_SSID>
password = <WIFI_PASSWORD>

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,password)


while not wlan.isconnected():
    print("Waiting for WiFi connection...")
    time.sleep(1)

print("WiFi connected:", wlan.ifconfig())

MQTT_BROKER = "<YOUR_CLUSTER_ADDRESS>.s1.eu.hivemq.cloud"
MQTT_PORT = <YOUR_PORT>
MQTT_USER = <YOUR_ID>
MQTT_PASS = <YOUR_PASSWORD>
MQTT_TOPIC = <YOUR_TOPIC> # ex. b"my/temp"
data = {"timestamp":time.time(), "temp":random.randint(5,40)} # change what you want
MQTT_PAYLOAD = json.dumps(data)

client = MQTTClient(
    client_id="pico-client",
    server=MQTT_BROKER,
    port=MQTT_PORT,
    user=MQTT_USER,
    password=MQTT_PASS,
    ssl=True,
    ssl_params={"server_hostname": MQTT_BROKER}  # for SNI
)

try:
    client.connect()
    print("MQTT connected.")
    client.publish(MQTT_TOPIC, MQTT_PAYLOAD, qos=1)
    print("Published.")
except Exception as e:
    print("MQTT Error:", e)


for i in range(1000):
    try:
        data['temp'] = random.randint(5,40)
        MQTT_PAYLOAD = json.dumps(data)
        client.publish(MQTT_TOPIC, MQTT_PAYLOAD, qos=1)
        print(f"Published. {MQTT_PAYLOAD}")
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)
    except Exception as e:
        print("MQTT Error:", e)
        client.disconnect()
        break
