import serial
import time
from pynput.keyboard import Key, Controller

# keyboard = Controller()

# def pauseGest(){
# keyboard.press(Key.space)
# keyboard.release(Key.space)
	
# }

# # Type 'Hello World' using the shortcut type method
# keyboard.type('Helo World')
# 

ser = serial.Serial('/dev/ttyACM0', 9600)
maxAcc = {insert threshhold}
pauseSens = {insert minimal angle to pause}
data = []
init = ser.readline()
string_n = init.decode()  
string = string_n.rstrip()

while True:
    b = ser.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    print(string)
    if(string[0] == "$")
    	data = []
    	data.append(string.split(","))	
	else:
		data.append(string.split(","))

    if(user looks away from screen):
    	pauseGest()
    elif(change in acceleration > maxAcc):
    	if(true):
    		do this
    	elif(true):
    		do this
    	elif(true):
    		do this
    	elif(true):
    		do this
    

ser.close()