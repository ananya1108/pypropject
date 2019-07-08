# summer course 

**Python Graph basics**
* Plot1.py:-Basic graph plotting      
* Plot2merge.py:-sublplot and merge graphs 
* Plot3axis.py:-use of plt.axis to define x and y axis size
* PLot4subplot.py:-use of subplot
* Plot5hito.py:-plotting histogram
* Plot6pie.py:-plotting pie chart 
* Plot7ecg.py:-graph reading data from ecg.csv file
* Plot8bar.py:-bar graph plotting
* Plot9live.py:-live graph, reading file example.txt
* Untitled.py:-changes graph when example.txt file data is updated and the graph is FTE design

**Raspberry Pi programms**
* RPIdht11_delay.py:-getting data from dht 11 and displaying output
* RPILED1.py:- turns on the led if sum of two numbers is odd
* RPILEDbasic.py:- turning on of LED on python3
* RPIclocdc_thingsboard.py:- controlling led from thingsboard localhost cloud
* RPImqtt_dht11pro.py:- displaying temperature and humidity collected by dht11 on thingsboard via MQTT
* RPIservo1.py:- servo motor program
* dht11.py:-printing temperature and humidity data to terminal
* button.py:-python3 code to test the working of button
* readdat.py:-~~tried reading data from thingspeak but didnt work~~
* readssssssdat.py:- ~~tried reading data from thingspeak again but didnt work( wrong logic used again)~~
* temp.py:-will print temperature and data same as dht11 but check code this worked and dht11 is sample

**MQTT/twilio/IoT**
* pubs.py:-publisher code for MQTT, works with app via hotspot(sophos blocks 1883) credit:-@pyropotato thankyou :+1: 
* smssend.py:-tried to send sms to phone from twilio but didnt work have to check
* thingspeak1.py:-read data from dht11 and prints temperature to field1 and humidity to field2
* trialtwilio.py:-again tried to send message through twilio
* twiliopro.py:-this is final twilio program , have to check (will mostly work)
> probably all twilio programms are same

**File/Database**
* file.py:- basic program for operation of read and write to file
* displaysql:- gets temperature and humidity data from dht11 raspberry Pi and saves to a database "sensordata" using sqlite3 in   pthon 
* plotsql:gets data stored in database "sensordata" and plots a graph "program not complete!!"
* TandHwrite.py:- takes temperature and humidity data and wtrites to readings.csv file @pyropotato thanks:+1:
* fetchsql:- fetching databse and printing using fetchall() from "fetching.db" "incomplete program"
* DB_sql_Static:- creating a database and storing data to "soisIOT.db"
* dynamicSQL:- storing dynamic data in database , i.e time , date and and randn variable in "dynamicDB.db"

**Calculator**
* Scratch_1.py:- basic python calculator 

**Arduino+RPi 3**
* aduino_sedning:- read dht11 readings from RPi using pyserial library and store into database "datafromArduino, decoding data     and using a delimiter is important.This is programmed on Rpi in python
* ArduinoSendingData:- this is programmed on Arduino to store and print dht11 readings i.e temperature and humidity, also a       delimiter is printed along with T&H.



