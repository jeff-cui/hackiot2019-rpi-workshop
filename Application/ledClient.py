# LED Client 
#
# This code runs on your VM and sends requests to the Raspberry Pi to turn on 
# and off the Grove LED using TCP packets.

import socket

def Main():
    #Set up host as Luis's RPI and port, CODE TO DELETE
    host = '192.168.1.126'
    port = 5000

    #Bind socket, CODE TO DELETE
    s = socket.socket() 
    s.connect((host,port))

    #Prompt for message, CODE TO DELETE
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