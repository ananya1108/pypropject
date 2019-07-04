import urllib2
import json
import time
import urllib

while True:
    abc=urllib.request.urlopen("https://api.thingspeak.com/channels/815194/feeds.json?results=2")
    response=TS.read()
    print(data)