# LED Server
# 
# This program runs on the Raspberry Pi and accepts requests to turn on and off
# the LED via TCP packets.

#Team Members:
#Jeff Cui 
#Luis Ortiz

#Insert Github repository link here.
#https://github.com/usc-ee250-fall2018/grovepi-lab03-gubohwatch3.git

import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../../Software/Python/')

import grovepi
import socket

def Main():
	#Setup host as Luis's RPI and port
    host = '192.168.1.126'
    port = 5000

    #Bind socket
    s = socket.socket()
    s.bind((host,port))

    #Initialize LED as digital port D7
    led = 7
    grovepi.pinMode(led,"OUTPUT")

    #Listen to connect
    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))

    #While true, receive data
    while True:
    	#Receive the data
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("From connected user: " + data)
        
        #Sendback message to check
        sendback = ""

        #If LED ON then turn on LED
        if(data == "LED_ON"): 
        	grovepi.digitalWrite(led,1)
        	sendback = "LED_ON Success"
        #Else if LED OFF then turn it off
        elif(data == "LED_OFF"):
        	grovepi.digitalWrite(led,0)
        	sendback = "LED_OFF Success"
        #Else, it's not good
        else:
        	sendback = "Command Not Recognized"

        #Send the response back
        c.send(sendback.encode('utf-8'))
    c.close()

if __name__ == '__main__':
    Main()