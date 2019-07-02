import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT,)
number1= input("first number:")
number2= input("\nsecond number:")
sum= number1+number2
print("\nif sum is odd led will turn on")
if sum%2==0:
    GPIO.output(11, False)
    print("\nsum is even")
else:
    GPIO.output(11, True)
    time.sleep(10)
    GPIO.output(11, False)
GPIO.cleanup()
