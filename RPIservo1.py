import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup("pin number",GPIO.OUT)

p=GPIO.PWM("pin number",50)
p.start(7.5)

try:
    while True:
        p.ChangeDutyCylce(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(2)
        p.ChangeDutyCycle(2.5)
        time.sleep(2)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
        
