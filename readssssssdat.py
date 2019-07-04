
import json
import time
import urllib.request

while True:
    abc=urllib.request.urlopen("https://api.thingspeak.com/channels/815194/feeds.json?results=2")

    response=TS.read()
    
    print(data)
