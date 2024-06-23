import RPi.GPIO as GPIO
import time


def main_locker():
    channel = 16
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)

    GPIO.output(channel, GPIO.HIGH) 

    time.sleep(60)

    GPIO.output(channel, GPIO.LOW)

 


