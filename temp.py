import Adafruit_DHT as dht
import time

# Configuration: Sensor Type and GPIO Pin (Physical 7)
sensor, pin = dht.DHT11, 4

while True:
    # Read returns (humidity, temperature) in that exact order
    h, t = dht.read_retry(sensor, pin)

    if h is not None and t is not None:
        print(f"Temp: {t:.1f}°C | Hum: {h:.1f}%")
    else:
        print("Sensor Error")

    time.sleep(2) # DHT11 requires a 2-second cooldown

# pip3 --version
# sudo apt install python3-pip
#pip3 install Adafruit_DHT
