import RPi.GPIO as GPIO
from hx711 import HX711
import time

# Define the pins connected to the HX711
DT_PIN = 12  # GPIO pin connected to DT
SCK_PIN = 21  # GPIO pin connected to SCK

# Disable GPIO warnings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Initialize the HX711 object
hx = HX711(dout_pin=DT_PIN, pd_sck_pin=SCK_PIN)

# Function to tare the scale
def tare():
    raw_data_list = [hx.get_raw_data() for _ in range(10)]  # Collect 10 readings
    averaged_raw_data = sum(raw_data_list) / len(raw_data_list)
    return averaged_raw_data[0]  # Return the first element (the actual value)

# Function to get the current weight
def get_weight(offset, reference_unit):
    raw_data = hx.get_raw_data()
    average_raw_data = sum(raw_data) / len(raw_data)
    weight = (average_raw_data - offset) / reference_unit
    return weight

# Initialize the scale
offset = tare()
print("Tare done! Add weight now...")

# Calibrate the reference unit (this is a placeholder value, you need to calibrate it)
reference_unit = 204  # Adjust this value based on known weight calibration

try:
    while True:
        # Read the current weight
        weight = get_weight(offset, reference_unit)
        print(f"Weight: {weight:.2f} grams")

        money = weight/6.1
        
        # Power down to save power
        hx.power_down()
        hx.power_up()
        time.sleep(0.5)

except (KeyboardInterrupt, SystemExit):
    print("Cleaning up...")
    GPIO.cleanup()
