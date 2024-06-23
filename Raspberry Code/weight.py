import RPi.GPIO as GPIO
import time

# Define the pins connected to the HX711
DT_PIN = 12  # GPIO pin connected to DT
SCK_PIN = 21  # GPIO pin connected to SCK

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DT_PIN, GPIO.IN)
GPIO.setup(SCK_PIN, GPIO.OUT)

def read_raw_data():
    """
    Read 24-bit raw data from HX711.
    """
    data = 0
    # Wait for DT pin to go low indicating data is ready
    while GPIO.input(DT_PIN) == 1:
        pass

    # Read 24 bits of data
    for _ in range(24):
        GPIO.output(SCK_PIN, True)
        data = (data << 1) | GPIO.input(DT_PIN)
        GPIO.output(SCK_PIN, False)

    # Set the channel and gain factor (1, 2, or 3 pulses for different gains)
    GPIO.output(SCK_PIN, True)
    GPIO.output(SCK_PIN, False)

    # Convert the 24-bit data to signed 32-bit integer
    if data & 0x800000:
        data |= ~0xFFFFFF

    return data

def read_average(count=10):
    """
    Read average of multiple raw data readings for better stability.
    """
    total = 0
    for _ in range(count):
        total += read_raw_data()
        time.sleep(0.01)  # Small delay between readings
    return total // count

def tare(count=15):
    """
    Tare the scale (set the zero point).
    """
    global offset
    offset = read_average(count)

def get_weight(count=10):
    """
    Get the current weight in grams.
    """
    value = read_average(count) - offset
    weight = value / reference_unit
    return weight

# Initialize the scale
offset = 0
reference_unit = 204  # This needs to be calibrated for your specific load cell

try:
    # Tare the scale to set the zero point
    tare()
    print("Tare done! Add weight now...")

    while True:
        weight = get_weight()
        if weight > 100000 or weight < -100000:
            # Discard outlier readings
            continue
        print(f"Weight: {weight:.2f} grams")
        time.sleep(1)  # Increased delay for stability

except KeyboardInterrupt:
    print("Cleaning up...")
    GPIO.cleanup()
