from luma.core.interface.serial import spi
from luma.led_matrix.device import max7219
from luma.core.render import canvas
from luma.core.legacy import show_message
import time

serial = spi(port=0, device=0)
device = max7219(serial, cascaded=1, block_orientation=90) 

print("Matrix Ready... Press CTRL+C to stop")

try:
    while True:
        with canvas(device) as draw:
            draw.rectangle((3, 3, 4, 4), outline="white", fill="white")
        time.sleep(1)
        
        with canvas(device) as draw:
            for i in range(8): draw.point((i, i), fill="white")
        time.sleep(1)

        with canvas(device) as draw:
            draw.rectangle((0, 0, 7, 7), outline="white")
        time.sleep(1)

        with canvas(device) as draw:
            points = [
                (1,7),(1,6),(1,5),(1,4),(1,3),(1,2),(1,1),
                (2,0),(3,0),(4,0),(5,0),
                (6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),
                (2,2),(3,2),(4,2),(5,2),
                (5,2),(5,3),(5,4),(5,5),(5,6),(5,7),
                (3,4),(4,4)
            ]
            for p in points: 
                draw.point(p, fill="white")
        time.sleep(2)

        show_message(device, " RUTA CS-IT ", scroll_delay=0.1)
        
except KeyboardInterrupt:
    device.clear()
    print("\nDisplay Cleared.")









#sudo raspi-config → Interface Options → SPI → Enable
#sudo reboot
#pip3 install luma.led_matrix
#Run code
#Pins: "1 — 6 — 19 — 24 — 23”
