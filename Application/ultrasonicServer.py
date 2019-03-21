#Ultrasonic Sensor Server
#
# This code runs on your VM and receives a stream of packets holding ultrasonic
# sensor data and prints it to stdout. Use a UDP socket here.

import socket

def Process1():
    #Setup variable "host" and "port"
    

    #Create socket "s" [below]



    #Start the receiving process
    print("Ultrasonic Server Started")
    while True:
    	#Receive data and print it
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')

        #Print our data [below]

    c.close()

if __name__ == '__main__':
    Process1()
    