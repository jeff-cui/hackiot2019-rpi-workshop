# Ultrasonic Sensor Client
# 
# This code runs on the Raspberry Pi. It should sit in a loop which reads from
# the Grove Ultrasonic Ranger and sends the reading to the Ultrasonic Sensor 
# Server running on your VM via UDP packets. 

#Team Members:
#Jeff Cui 
#Luis Ortiz

#Insert Github repository link here.
#https://github.com/usc-ee250-fall2018/grovepi-lab03-gubohwatch3.git

import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are able to successfully `import grovepi`
sys.path.append('../../../Software/Python/')

import grovepi
import socket
import time

def Main():
    #Change the host and port as needed. Client port use 1024
    #Host is RPi IP address
    host = '192.168.1.126'
    port = 1024

    #Server address is LAN host OS
    server_addr = '192.168.1.109'

    #Bind socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind((host,port))

    #Connect ranger to digital port D4
    ultrasonic_ranger = 4
    grovepi.pinMode(ultrasonic_ranger,"INPUT")

    #Enter the destination port which is 8050 or 8051
    dst_port = input("destination port-> ")

    while True:
        #Specifies udpServer1 or 2
        server = (server_addr, int(dst_port))

        #Read ultrasonic and format for transmission
        reading = grovepi.ultrasonicRead(ultrasonic_ranger)
        message = str(reading) + " cm"

        #Print to terminal
        print("RPi: " + message)

        #Send it to the server
        s.sendto(message.encode('utf-8'), server) 

        #Sleep and then go again
        time.sleep(0.2)
    s.close()

if __name__ == '__main__':
    Main()
