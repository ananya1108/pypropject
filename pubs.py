import paho.mqtt.client as mqtt
import datetime
import sys
import Adafruit_DHT
import csv

broker_address = "test.mosquitto.org"
client = mqtt.Client("RPI")
client.connect(broker_address,1883,60)
count=1
while (count==1):
    print("This code works")
    humidity, tempreature = Adafruit_DHT.read_retry(11,02)
    client.publish("trial/temp",str(tempreature))
    client.publish("trial/humidity",str(humidity))
    
        
