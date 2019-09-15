#PierreIsHere
#14/09/2019
#main.py
#creating driver code to parse arduino serial data and manipulate websites
#based off of recieved data
import serial
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#cont - wether or not the the input is continuous
#side direction of video scrubbing
#bar = location of video bar
def scrub(cont,side,bar):   
    if(cont == False):
        if(side):
            bar.send_keys(Keys.ARROW_RIGHT)
        else:
            bar.send_keys(Keys.ARROW_LEFT)
    else:
        if(side):
            while(minRoll <=angle <= maxRoll):
                browser.send_keys(Keys.ARROW_RIGHT)
        else:
            while(minRoll <=angle <= maxRoll):
                browser.send_keys(Keys.ARROW_LEFT) 

#buttons can be next,prev,(fullscreen)/minimize,(play)/pause
#broswer defines the action location
def buttonClick(button,browser):
    browser.find_element_by_class_name('ytp-'+button+'-button').click()
         
#Initialization
ser = serial.Serial('COM6', 9600)

browser = webdriver.Chrome("chromedriver.exe")
browser.get('https://www.youtube.com/watch?v=j8umNI8gtlA')

data = []
# maxAcc = {insert threshhold}
# pauseSens = {insert minimal angle to pause}
# maxAngle = {insert max angle of double}

#Main Loop
#Yaw,Pitch,Roll
while True:
    b = ser.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    print(string)
    #re initializing the array to save on ram only updating when accelerometer recalibrates
    if(string[0] == "0"):
        data = []
        temp=string.split(",")
        data.append([int(float(temp[0])),int(float(temp[1])),int(float(temp[2]))])   
    else:
        temp=string.split(",")
        data.append([int(float(temp[0])),int(float(temp[1])),int(float(temp[2]))])
    bar = browser.find_element_by_class_name("ytp-progress-bar ")
    if(data[0][0]>35):
        scrub(0,1,bar)
    elif(data[0][0]>35):
        scrub(0,0,bar)
    elif(data[0][0]>35):
        buttonClick("play",browser)
    elif(data[0][0]>35):
        buttonClick("next",browser)
    elif(data[0][0]>35):
        buttonClick("prev",browser)
    elif(data[0][0]>35):
        buttonClick("fullscreen",browser)
#ser.close()
#browser.close()
