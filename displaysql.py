import sqlite3
import json
import time
import Adafruit_DHT
import random


sensor=Adafruit_DHT.DHT11

gpio=02

a=[]
while True:
    humidity, temperature= Adafruit_DHT.read_retry(sensor,gpio)


    #if humidity is not None and temperature is not None:
     #   print('Temp={0:0.1f}*c Humidity={1:0.1f}%' .format(temperature, humidity))
    #else:
     #   print("failed to get reading. Try again!")

    a=temperature
    b=humidity
    print(a)
    print(b)
    time.sleep(5)

#sql connection starts
    
    conn=sqlite3.connect("sensordata.db") #database created

    c=conn.cursor() #cursor created
    def create_table():
        c.execute("CREATE TABLE IF NOT EXISTS dhtreadings(D INT AUTO_INCREMENT,Temperature REAL,Humidity REAL,Value REAL,PRIMARY KEY(D))")

    def dynamic_data_entry():
        Temperature=float(a)
        Humidity=float(b)
        #date=str(datetime.datetime.now(Datestamp).strftime("%Y-%m-%d %H:%M:%S"))
        Value=random.randrange(0,100)
        #Srno=int(x=0)

        c.execute("INSERT INTO dhtreadings(Temperature,Humidity,Value) VALUES(?,?,?)",
                  (a,b,Value))
        conn.commit()
    for i in range(100):
        create_table()
        dynamic_data_entry()
        time.sleep(1)
    c.close()
    conn.close()
