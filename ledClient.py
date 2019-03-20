# LED Client 
#
# This code runs on yoru VM and sends requests to the Raspberry Pi to turn on 
# and off the Grove LED using TCP packets.

#Team Members:
#Jeff Cui 
#Luis Ortiz

#Insert Github repository link here.
#https://github.com/usc-ee250-fall2018/grovepi-lab03-gubohwatch3.git

import socket

def Main():
    #Set up host as Luis's RPI and port
    host = '192.168.1.126'
    port = 5000

    #Bind socket
    s = socket.socket() 
    s.connect((host,port))

    #Prompt for message
    message = input("Input for LED-> ")
    while message != 'q':
    	#Send the message
        s.send(message.encode('utf-8')) 
         
        #Receive back the server response
        data = s.recv(1024).decode('utf-8') 
        print("Received from LED server: " + data)

        #Take another message
        message = input("Input for LED-> ")
    s.close()

if __name__ == '__main__':
    Main()