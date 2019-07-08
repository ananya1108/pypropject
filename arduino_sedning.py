import serial #imports pyserial library which is used for serial communication
import sqlite3 #for database storage
import time

arduino=serial.Serial("/dev/ttyACM0",9600) #used dmesg on terminal to check port on which arduino is connected

#@ is used after humidity
#temp1=[]
#humid1=[]

while True:
    data=(arduino.readline().decode().strip()) #will print string data #.readline() shows output of arduino,.decode() will convert data coming from bytes ,.strip() will remove whitespaces
    data=data.split("@") #delimiter used to divide data into list
    #print(data)        #data is now a list
    humidity=float(data[0])   #typecast
    temperature=float(data[1]) #typecast
    
#storing the above data in a databse

    #snippet from sensordata.db edited
    conn=sqlite3.connect("datafromARDUINO.db") #database created

    c=conn.cursor() #cursor created
    def create_table():
        c.execute("CREATE TABLE IF NOT EXISTS ArduinoReadings(Temperature REAL,Humidity REAL)")

    def dynamic_data_entry():
        Temperature=float(temperature)
        Humidity=float(humidity)
        #date=str(datetime.datetime.now(Datestamp).strftime("%Y-%m-%d %H:%M:%S"))
        #Value=random.randrange(0,100)
        #Srno=int(x=0)

        c.execute("INSERT INTO ArduinoReadings(Temperature,Humidity) VALUES(?,?)",
                  (temperature,humidity))
        conn.commit()
    for i in range(100):
        create_table()
        dynamic_data_entry()
        time.sleep(1)
    c.close()
    conn.close()
