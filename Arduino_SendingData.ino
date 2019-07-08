#include "dht.h"
#define dht_apin 7// digital pin;- sensor is connected to
 
dht DHT;
 
void setup(){
 
  Serial.begin(9600);
  delay(500);//Delay to let system boot
  //Serial.println("DHT11 Humidity & temperature Sensor\n\n");
  delay(1000);//Wait before accessing Sensor
  //int humidity_arduino,temperature_arduino;
}//end "setup()"
 
void loop(){
                               //Start of Program 
    DHT.read11(dht_apin);
    
  //Serial.print("Current humidity = ");
    Serial.print(DHT.humidity);
    Serial.print("@");
    //Serial.print("temperature = ");
    Serial.println(DHT.temperature); 
    //Serial.println("@");
    //int humidity_arduino=DHT.humidity;          //typecaste string to int
    //int temperature_arduino=DHT.temperature;    //same done here
   
    delay(3000);//Wait 3 seconds before accessing sensor again.
 
  //Fastest should be once every two seconds.
 
}// end loop() 
