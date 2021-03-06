import threading
import sys
import socket
from client import *

print("Server Start")
host = 'localhost'
port = 12342


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port)) #bind the socket
sock.listen(1) #listen for incoming connection

while True :
    try:
        print('Waiting for connection')
        conn, client = sock.accept()
        print ('Incoming Connection : ' + str(conn))
        thread = Handler(client,conn)
        thread.start()

    except KeyboardInterrupt:
        break

print ("\nExiting Server")

