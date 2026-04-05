#sudo apt install python3-pip
#pip3 install telepot

#"15 — 9" for red, "16 — 6" for yellow

import telepot
from telepot.loop import MessageLoop
from datetime import datetime
import RPi.GPIO as GPIO
from time import sleep

red = 22
yellow = 23

now = datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0)

GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow, 0)

def action(msg):
    chat_id = msg["chat"]["id"]
    command = msg["text"]
    print("Received: " + command)
    
    if "on" in command.casefold():
        message = "on "
        if "red" in command.casefold():
            message = message + "red"
            GPIO.output(red, 1)
        elif "yellow" in command.casefold():
            message = message + " yellow"
            GPIO.output(yellow, 1)
        
        message = message + " light(s)"
        telegram_bot.sendMessage(chat_id, message)

    if "off" in command.casefold():
        message = "off "
        if "red" in command.casefold():
            message = message + " red"
            GPIO.output(red, 0)
        elif "yellow" in command.casefold():
            message = message + " yellow"
            GPIO.output(yellow, 0)
        
        message = message + " light(s)"
        telegram_bot.sendMessage(chat_id, message)

telegram_bot = telepot.Bot("YOUR BOT TOKEN")
print(telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()

print("Telegram Bot is active and listening...")

try:
    while True:
        sleep(10)
except KeyboardInterrupt:
    print("\nProgram stopped by user")
finally:
    GPIO.output(red, 0)
    GPIO.output(yellow, 0)
    GPIO.cleanup()
