# Ultrasonic Sensor Client
# 
# This code runs on the Raspberry Pi. It should sit in a loop which reads from
# the Grove Ultrasonic Ranger and sends the reading to the Ultrasonic Sensor 
# Server running on your VM via UDP packets. 

import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are able to successfully `import grovepi`
sys.path.append('../../../Software/Python/')

import grovepi
import socket
import time

def Main():
    #Create variable "host" and "port" [below]
    

    #Setup server address [below]
    

    #Bind socket "s" [below]

    #Connect ranger to digital port D4
    ultrasonic_ranger = 4
    grovepi.pinMode(ultrasonic_ranger,"INPUT")

    #Create variable "dst_port" that takes in destination port via input function [below]
    

    while True:
        #Specifies which udp server to send to via variable "server" [below]
        

        #Read ultrasonic and format for transmission
        reading = grovepi.ultrasonicRead(ultrasonic_ranger)
        message = str(reading) + " cm"

        #Print to terminal
        print("RPi: " + message)

        #Send it to the server
        s.sendto(message.encode('utf-8'), server) 

        #Sleep to delay [below]
        
    s.close()

if __name__ == '__main__':
    Main()
