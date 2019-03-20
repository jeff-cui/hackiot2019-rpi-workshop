"""TCP Client"""

import socket

def Main():
    """127.0.0.1 is the loopback address. Any packets sent to this address will
    essentially loop right back to your machine and look for any process 
    listening in on the port specified."""
    host = '127.0.0.1'
    port = 5000

    #Create a socket and connect to our host and port, this will then connect to our server
    s = socket.socket() #by default, the socket constructor creates an TCP/IPv4 socket
    s.connect((host,port))

    """Input messages to send to server"""
    message = input("-> ")

    """As long as message is not q then we send to the server, and display the feedback from the server"""
    while message != 'q':
        #Send
        s.send(message.encode('utf-8')) 
        
        #Receive feedback
        #1024 is the receive buffer size. It's enough for us, and it's a nice number. 
        data = s.recv(1024).decode('utf-8') 
        print("Received from server: " + data)

        #Get ready to send another message
        message = input("-> ")
    s.close()

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 tcpClient.py` in terminal, this if-statement will be 
true"""
if __name__ == '__main__':
    Main()