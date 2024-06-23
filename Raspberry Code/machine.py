# machine.py
import RPi.GPIO as GPIO

class Pin:
    IN = GPIO.IN
    OUT = GPIO.OUT
    PULL_UP = GPIO.PUD_UP
    PULL_DOWN = GPIO.PUD_DOWN

    def __init__(self, pin, mode=-1, pull=-1):
        self.pin = pin
        # Use BCM numbering
        GPIO.setmode(GPIO.BCM)  
        if mode in [self.OUT, self.IN]:
            if pull in [self.PULL_UP, self.PULL_DOWN]:
                GPIO.setup(pin, mode, pull_up_down=pull)
            else:
                GPIO.setup(pin, mode)
        else:
            raise ValueError("Invalid mode")

    def value(self, val=None):
        if val is None:
            return GPIO.input(self.pin)
        else:
            if GPIO.gpio_function(self.pin) == GPIO.OUT:
                GPIO.output(self.pin, val)
            else:
                raise ValueError("Cannot set value on input mode")

# Ensure GPIO cleanup at exit
import atexit
atexit.register(GPIO.cleanup)
