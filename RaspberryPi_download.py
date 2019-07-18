import os
import time
import urllib3   #https://urllib3.readthedocs.io/en/latest/
import ast
import json
import paho.mqtt.client as mqtt
import datetime
import sys
import Adafruit_DHT
import csv

http = urllib3.PoolManager()
x = input("Number of Entries: ")
x = int(x)
broker_address = "test.mosquitto.org"
client = mqtt.Client("RPI")
client.connect(broker_address,1883,60)
try:
    url = "https://api.thingspeak.com/channels/825264/feeds.json?api_key=KS33OLLO5XYAKRBC&results=%i" %(x)
    response = http.request('GET',url)
    print(type(response.data))
    data = response.data #byte
    data = data.decode('utf8') #converting byte to string
    print(type(data))
    data = json.loads(data) #convert to dictionary
    #print (data)
    ch_name = data["channel"]["name"] #channel name
    ch_id = data["channel"]["id"] #channel id
    ch_description = data["channel"]["description"]
    field1_name = data["channel"]["field1"]
    field2_name = data["channel"]["field2"]
    print("")
    print ("Name: " + ch_name)
    print ("ID: " + str(ch_id))
    print ("Description: " + ch_description)
    for x in data["feeds"]:
        entry_id = x["entry_id"]
        time = x["created_at"]
        field1 = x["field1"]
        field2 = x["field2"]
        count=1
        while (count==1):
            broker_address = "test.mosquitto.org"
            client = mqtt.Client("RPI")
            client.connect(broker_address,1883,60)
            client.publish("trial/temp",(field1))
            client.publish("trial/humidity",(field2))
        print('ID = {0}  Time = {1}  {4} = {2}  {5} = {3}' .format(entry_id,time,field1,field2,field1_name,field2_name)) #change name accordingly
    #time.sleep(1)
    print(field1)
     #broker_address = "test.mosquitto.org"
    #client = mqtt.Client("RPI")
    #client.connect(broker_address,1883,60)
    #count=1
    #while (count==1):
     #   print("This code works")
        #humidity, tempreature = Adafruit_DHT.read_retry(11,02)
        #client.publish("trial/temp",str(field1))
        #client.publish("trial/humidity",str(field2))
        


except Exception as e:
        
        print("Exeception occured:{}".format(e))
