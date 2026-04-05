import RPi.GPIO as GPIO
import time

# Configuration (BCM numbering)
GPIO.setmode(GPIO.BOARD)

# Now use the PHYSICAL pin numbers
# Physical Pin 11 is BCM 17
# Physical Pin 12 is BCM 18
FLAME, ALERT = 11, 12 

GPIO.setup(FLAME, GPIO.IN)
GPIO.setup(ALERT, GPIO.OUT)

print("Flame Sensor Monitoring... (CTRL+C to stop)")

try:
    while True:
        # Active-Low: 0 = Flame, 1 = Safe
        is_flame = GPIO.input(FLAME) == 0
        
        GPIO.output(ALERT, is_flame)
        status = "ALERT ON! Flame Detected" if is_flame else "Safe: No Flame"
        print(f"[{time.strftime('%H:%M:%S')}] {status}")
        
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nSystem Disarmed")
finally:
    GPIO.cleanup()



#Pins to remember: "1 — 6 — 11" for sensor, "12 — 14" for LED
