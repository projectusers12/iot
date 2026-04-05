import RPi.GPIO as GPIO
import time

# Configuration
SENSOR, LED = 16, 18
BLINK_MODE = True  # Set to False for "Always On", True for "Blinking"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SENSOR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

print(f"IR Sensor Ready (Mode: {'Blink' if BLINK_MODE else 'Solid'})...")

try:
    while True:
        if GPIO.input(SENSOR) == 0:  # Object detected
            print("Object Detected")
            GPIO.output(LED, True)
            
            if BLINK_MODE:
                time.sleep(0.3)
                GPIO.output(LED, False)
                time.sleep(0.3)
        else:
            GPIO.output(LED, False)
            
except KeyboardInterrupt:
    print("\nProgram stopped by user")
finally:
    GPIO.cleanup()

#4-6-16-18-20" — the 5 pin numbers to remember
#5v
