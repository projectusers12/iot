import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)  
ledPin = 15 # Physical Pin 15 (which is BCM 22)

GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, False) 

print("Single LED Blinking... Press CTRL+C to stop")

try:
    while True:
        GPIO.output(ledPin, True)  
        print("LED ON")
        sleep(1)                   
        
        GPIO.output(ledPin, False) 
        print("LED OFF")
        sleep(1)                   

finally:
    GPIO.cleanup() # Safety: Resets the pins
