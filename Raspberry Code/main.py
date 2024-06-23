from RPLCD.i2c import CharLCD
import time
from fingerprint import get_fingerprint
from display import *
from keypad import *
from ch import verification_code
from locker import *
from sendSMS import *
from moneySend import *


safeIsClosedFlag    = True
fingerprintFlag     = False
faceRecognitionFlag = False
keyEnteredFlag      = False


def resetFlags():
    global safeIsClosedFlag      
    global fingerprintFlag       
    global faceRecognitionFlag   
    global keyEnteredFlag        
    safeIsClosedFlag      = True
    fingerprintFlag       = False
    faceRecognitionFlag   = False  
    keyEnteredFlag        = False
    


def fingerMain():
    #print that we are in the beggining state
    printFirstState()

    #print the message for introducing the fingerprint
    printIntroduceFingerprint()

    remainedTries = 3
    
    while remainedTries != 0:
        if get_fingerprint():
            printIsAMatchFingerprint()
            return True
        else:
            printFingerprintMissed()
            remainedTries -= 1
            printIntroduceFingerprint()
    
    if remainedTries == 0:
        printPersonFailed()
        printSafeIsBlocked()
        
    return False


def faceRecoMain():
    printSecondState()
    return True

    
def keyMain():
    global goodFormatFlag
    global wrongFormatFlag
    global sentToEarlyFlag
    global keyEnteredFlag    
    global verification_code
    global global_key
    
    printThirdState()
    printEnterKey()
    
    key = scan_key()
    
    print(verification_code)
    print(key)
    
    if int(verification_code) == key:
        keyEnteredFlag = True
        print("worked")
    else:
        if key == 1:
            printSecurityResetAndBlock()
            resetFlags()
        else:
            print("???")
            resetFlags()
            global_key = 0
    
    
        
    

def Main():
    global safeIsClosedFlag
    global fingerprintFlag
    global faceRecognitionFlag
    global keyEnteredFlag
    global securityFlag
    while safeIsClosedFlag is True:
        fingerprintFlag = fingerMain()
        while fingerprintFlag is True:
            faceRecognitionFlag = faceRecoMain()
            while faceRecognitionFlag is True:
                main_SMS()
                keyMain()
                if keyEnteredFlag is True:
                    printSafeWillOppen()
                    main_locker()
                    main_money()
    


Main()
