"""UDP Client"""

import socket

def Main():
    # Change the host and port as needed.
    host = '10.0.2.15'
    port = 1023

    #Establish the UDP Server IP addresses
    server_addr = '10.0.2.15'

    #Create and bind sockets
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind((host,port))

    # UDP is connectionless, so a client does not formally connect to a server
    # before sending a message.

    #Input our destination port and message
    dst_port = input("destination port-> ")
    message = input("message-> ")

    #We send our messages
    while message != 'q':
        #tuples are immutable so we need to overwrite the last tuple
        server = (server_addr, int(dst_port))

        # for UDP, sendto() and recvfrom() are used instead
        s.sendto(message.encode('utf-8'), server) 

        #We take our feedback data and display
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received from server: " + data)

        #Send another message
        dst_port = input("destination port-> ")
        message = input("message-> ")
    s.close()

if __name__ == '__main__':
    Main()