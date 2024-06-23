import smbus
from RPLCD.i2c import CharLCD
import time

# Adjust these parameters based on your specific LCD
I2C_ADDR = 0x27  # Typically the I2C address for 16x2 LCD
I2C_PORT = 1     # Default I2C port on Raspberry Pi

# Initialize the LCD
lcd = CharLCD('PCF8574', I2C_ADDR, port=I2C_PORT,
              cols=16, rows=2, charmap='A00')

def lcd_clear():
    """Clear the LCD display."""
    lcd.clear()

def lcd_write_string(message, line=0, col=0):
    """
    Write a string to the LCD.
    
    :param message: The string to display
    :param line: Line number (0 or 1 for a 2-line display)
    :param col: Column number (0 to 15 for a 16-column display)
    """
    lcd.cursor_pos = (line, col)
    lcd.write_string(message)

def print_first_state():
    """Display the 'Fingerprint state!' message."""
    lcd_clear()
    lcd_write_string("Fingerprint state!", line=0, col=0)
    time.sleep(5)

def print_weight(weight):
    """Display the weight on the LCD."""
    lcd_clear()
    lcd_write_string(f"Weight: {weight:.2f}g", line=0, col=0)


print_first_state()
