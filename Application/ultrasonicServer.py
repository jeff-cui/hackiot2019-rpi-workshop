#Ultrasonic Sensor Server
#
# This code runs on your VM and receives a stream of packets holding ultrasonic
# sensor data and prints it to stdout. Use a UDP socket here.

import socket

def Process1():
    #Port is 9005 and host is VM IP address 
    host = '10.0.2.15'
    port = 9005

    #Bind socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    #Start the receiving process
    print("Ultrasonic Server Started")
    while True:
    	#Receive data and print it
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("VM: " + data)
    c.close()

if __name__ == '__main__':
    Process1()
    