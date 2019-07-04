import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from gpiozero import Button
button= Button(3)
button.wait_for_press()
print("you pressed me")
    
