"""UDP Server 1"""

import socket

def Process1():
    # Change the host and port as needed. Host is the VM's IP address
    host = '10.0.2.15'
    port = 9000

    #Create and bind our socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    print("Process 1 Server Started")

    #While server is on, take in any data and print out the message and where it's from
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message From: " + str(addr))
        print("From connected user: " + data)

        #Send back feedback to original sender
        data = data.upper()
        print("Sending: " + data)
        s.sendto(data.encode('utf-8'), addr)
    c.close()

if __name__ == '__main__':
    Process1()
