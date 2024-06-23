from machine import Pin
import time

#Create the map between keypad buttons and characters
matrix_key = [ ['1', '2', '3', 'A'],
               ['4', '5', '6', 'B'],
               ['7', '8', '9', 'C'],
               ['*', '0', '#', 'D']]

#Pin connection
keypad_row = [5, 6, 13, 26]
keypad_col = [4, 17, 27, 22]

#Assign GPIO pins and setup input and outputs
#We need the 2 lists to set up pins such as Rows for output and column for input
pin_row = []
pin_col = []

for x in range(0, 4):
    pin_row.append(Pin(keypad_row[x], Pin.OUT))
    pin_row[x].value(1)
    pin_col.append(Pin(keypad_col[x], Pin.IN, Pin.PULL_DOWN))
    

# Variable to store the last pressed key
last_pressed_key = None
prev_key_counter = 0
key_counter      = 0
prev_global_key  = 0
global_key       = 0

goodFormatFlag   = False
wrongFormatFlag  = False
sentToEarlyFlag  = False
securityFlag     = False

def scan_key():
    global last_pressed_key
    global global_key
    global prev_global_key
    global key_counter
    global prev_key_counter
    global goodFormatFlag
    global wrongFormatFlag
    global sentToEarlyFlag
    
    while goodFormatFlag is False and wrongFormatFlag is False and sentToEarlyFlag is False:
        for row in range(4):
            for col in range(4):
            
                #set the current row to High
                pin_row[row].value(1)
            
                #Check to see if the col pin voltage is high
                if pin_col[col].value() == 1:
                    if col == 3:
                        #we will consider 'A' as 'Delete last inserted character from the key' button
                        if row == 0:
                            global_key   = prev_global_key
                            if key_counter > 0:
                                key_counter = prev_key_counter
                        #we will consider 'B' as 'Delete all the inserted characters from the key' button
                        if row == 1:
                            global_key  = 0
                            key_counter = 0
                            prev_global_key = 0
                        #we will consider 'C' as 'Fake' button -> do nothing actually to the key and the counter
                        if row == 2:
                            time.sleep(0.5)
                        #we will consider 'D' as 'Send key' button
                        if row == 3: 
                            if key_counter == 4:
                                goodFormatFlag  = True
                                return global_key
                            else:
                                sentToEarlyFlag = False
                                return 0
                    else:
                        if key_counter == 4:
                            wrongFormatFlag = True
                            return 0
                        else:
                            if matrix_key[row][col] == '*' or matrix_key[row][col] == '#':
                                return 1
                            else:
                                if key_counter > 0:
                                    prev_global_key  = global_key
                                    prev_key_counter = key_counter
                                # Store the pressed key
                                last_pressed_key = matrix_key[row][col]
                                global_key = global_key * 10 + int(last_pressed_key)
                                key_counter += 1
                                print("Current key:", global_key)
                                print("Current counter:", key_counter)
                
                                # This is the debounce delay
                                time.sleep(1)
                pin_row[row].value(0)
            
    
print("done")
print(global_key)
print(key_counter)
print(goodFormatFlag)
print(sentToEarlyFlag)
print(wrongFormatFlag)
print(securityFlag)
                    
    
