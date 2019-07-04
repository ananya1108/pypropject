import os
import time
#import serial
import urllib2
import Adafruit_DHT
while 1:
    try:
        humidity,temperature=Adafruit_DHT.read(11,2) #(sensor,GPIO pin number)
        print('Humidity=%f'% humidity)
        print('Temperature=%f'% temperature)
        print('----------------------------------')
        baseURL='https://api.thingspeak.com/update?api_key=BDSXA56NHQYRNS5Q'
        
        g=urllib2.urlopen(baseURL+ '&field1=%f,&field2=%f' % (temperature, humidity))
        print('----------------------------------')
        time.sleep(5)
    except:
        pass
        
