# IoT Project

**NodeMCU_uploading.ino**
* Code for uploading DHT 11 readings to the thingspeak server , also buzzer will go on if an object is placed in front of the PIR sensor

**RaspberryPi_download.py**
* This program will read data from thingspeak server and will upload it to the Mosquitto cloud using MQTT protocol
