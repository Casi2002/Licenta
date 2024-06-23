from RPLCD.i2c import CharLCD
import time
#from fingerprint import get_fingerprint

# Define the LCD using the I2C address and the correct columns and rows
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

# Clear the display
lcd.clear()

# Write some text to the LCD
#remainedTries = 3
#positiveFinger = False
#lcd.write_string("Fingerprint step")
#time.sleep(5)
#while remainedTries != 0 and positiveFinger is False:
#  if get_fingerprint():
#      lcd.clear()
#      lcd.write_string("Match!")
#      positiveFinger = True
#  else:
#      lcd.clear()
#     lcd.write_string("Try again")
#      remainedTries -= 1
#if remainedTries == 0:
#      lcd.clear()
#      lcd.write_string("Wrong person!")
# Clear the display and write new text
#lcd.clear()
#lcd.write_string('Raspberry Pi')
#time.sleep(5)

# Clear the display one more time
#lcd.clear()

def printFirstState():
	lcd.clear()
	lcd.write_string("Fingerprint state!")
	time.sleep(5)
	
def printIntroduceFingerprint():
	lcd.clear()
	lcd.write_string("Introduce fingerprint!")


def printIsAMatchFingerprint():
	lcd.clear()
	lcd.write_string("Authentification successfull!")
	time.sleep(5)


def printFingerprintMissed():
	lcd.clear()
	lcd.write_string("Fingerprint failed!")
	time.sleep(5)


def printPersonFailed():
	lcd.clear()
	lcd.write_string("Wrong person!")
	time.sleep(5)


def printSafeIsBlocked():
	lcd.clear()
	lcd.write_string("Safe Blocked for 2 min!")
	time.sleep(120)
	

def printSecondState():
	lcd.clear()
	lcd.write_string("FaceID state!")
	time.sleep(5)


def printThirdState():
	lcd.clear()
	lcd.write_string("Key state!")
	time.sleep(5)


def printEnterKey():
	lcd.clear()
	lcd.write_string("Enter the Key!")


def printSecurityResetAndBlock():
	lcd.clear()
	lcd.write_string("Security reset!")
	time.sleep(5)
	printSafeIsBlocked()


def printSafeWillOppen():
	lcd.clear()
	lcd.write_string("The safe will oppen!")
	time.sleep(5)
