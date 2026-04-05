import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
ledPin1 = 15 # Physical Pin 15 (Red LED)
ledPin2 = 11 # Physical Pin 11 (Yellow/Green LED)

GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)

print("Double LED Alternating... Press CTRL+C to stop")

try:
    while True:
        
        GPIO.output(ledPin1, True)  
        GPIO.output(ledPin2, False) 
        print("LED 1 ON  | LED 2 OFF")
        sleep(1)

       
        GPIO.output(ledPin1, False) 
        GPIO.output(ledPin2, True)  
        print("LED 1 OFF | LED 2 ON")
        sleep(1)

finally:
    GPIO.cleanup()
