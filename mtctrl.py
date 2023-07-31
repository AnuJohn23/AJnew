import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)
GPIO.setup(24, GPIO.OUT) 
GPIO.setup(23, GPIO.OUT)


while True:
     button_state = GPIO.input(17)
     if button_state == False:
         GPIO.output(24, True)
         GPIO.output(23, False)
         print('Button Pressed...')
     else:
         GPIO.output(24, False)
         GPIO.output(23, False)
         time.sleep(2)
         GPIO.output(24, True)
         GPIO.output(23, False)
         time.sleep(2)


