# LED Server
# 
# This program runs on the Raspberry Pi and accepts requests to turn on and off
# the LED via TCP packets.

import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../../Software/Python/')

import grovepi
import socket

def Main():
	#Create variable "host" and variable "port" [below]
    


    #Create and bind socket "s" [below]


    #Initialize LED as digital port D7
    led = 7
    grovepi.pinMode(led,"OUTPUT")

    #Listen to connect on socket "s" [below]
    

    print("Connection from: " + str(addr))

    #While true, receive data
    while True:
    	#Receive the data
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("From connected user: " + data)
        
        #Initialize sendback message variable "sendback" [below]
        

        #If LED ON then turn on LED, fill in the blanks below
        if(data == ""): 
        	grovepi.digitalWrite(led,1)
        	sendback = ""
        #Else if LED OFF then turn it off, fill in the blanks below
        elif(data == ""):
        	grovepi.digitalWrite(led,0)
        	sendback = ""
        #Else, it's not good, fill in the blank
        else:
        	sendback = ""

        #Send the "sendback" back [below]
        
    c.close()

if __name__ == '__main__':
    Main()