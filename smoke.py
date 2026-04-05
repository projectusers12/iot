#Pins: "2/4 — 6 — 11" for sensor, "13 — 14" for LEDs
import RPi.GPIO as GPIO
import time

# --- MAPPING ---
# BCM 17 is Physical Pin 11
# BCM 27 is Physical Pin 13
SMOKE_D0 = 11   
LED_PIN = 13    

GPIO.setmode(GPIO.BOARD) # Changed from BCM to BOARD
GPIO.setup(SMOKE_D0, GPIO.IN) 
GPIO.setup(LED_PIN, GPIO.OUT)

print("Smoke Sensor (MQ) is warming up... (20s)")
GPIO.output(LED_PIN, False)
time.sleep(20)

print("System Ready - Monitoring...")

try:
    while True:
        # Check if sensor sends 0 (Active-Low detection)
        if GPIO.input(SMOKE_D0) == 0:
            print("SMOKE/GAS DETECTED!")
            GPIO.output(LED_PIN, True)
        else:
            print("Air is clean")
            GPIO.output(LED_PIN, False)

        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    GPIO.cleanup()
