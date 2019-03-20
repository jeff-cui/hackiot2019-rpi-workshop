"""TCP Server"""

import socket

def Main():
    """127.0.0.1 is the loopback address. Any packets sent to this address will
    essentially loop right back to your machine and look for any process 
    listening in on the port specified."""
    host = '127.0.0.1'

    """We choose port 5000 because all ports lower could be defined for 
    other protocols, likely nothing will be sent on 5000"""
    port = 5000

    """Create a socket and bind it to our host and port"""
    s = socket.socket()
    s.bind((host,port))

    """TCP function of listening to connect"""
    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))

    """Receive messages from the client and send all uppercase of it back to the client"""
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break

        #Print received message
        print("From connected user: " + data)

        #Uppercase the message and send it back
        data = data.upper()
        print("Sending: " + data)
        c.send(data.encode('utf-8'))
    c.close()

if __name__ == '__main__':
    Main()