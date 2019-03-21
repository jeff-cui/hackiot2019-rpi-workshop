# LED Client 
#
# This code runs on your VM and sends requests to the Raspberry Pi to turn on 
# and off the Grove LED using TCP packets.

import socket

def Main():
    #Set up variable "host" and variable "port" [below]


    #Connect socket variable "s" [below]


    #Prompt for variable "message" with input function [below]


    while message != 'q':
    	#Send the message
        s.send(message.encode('utf-8')) 
         
        #Receive back the server response
        data = s.recv(1024).decode('utf-8') 
        print("Received from LED server: " + data)

        #Take another message [below]
        
        
    s.close()

if __name__ == '__main__':
    Main()