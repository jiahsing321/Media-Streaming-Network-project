#!/usr/bin/env python
import socket

#Send media selection to server
s = socket.socket()
host = '10.0.0.2'
port = 12345
s.connect((host, port))

print("Input the media file to render:\n")
print("BillOfRights.txt\n")
print("Constitution.txt\n")
print("DeclarationOfIndependence.txt\n")
print("GettysburgAddress.txt\n")
selection = input()

s.send(selection.encode())
s.close()

#Get confirmation from server when the file has been sent to the renderer and the renderer is ready to be controlled

s2 = socket.socket()
host2 = ''
port2 = 12348

s2.bind((host2, port2))
s2.listen(5)
c, addr = s2.accept()     # Establish connection with client

print (c.recv(1024).decode('utf-8'))

s2.close()

#Make connection to tbe renderer so commands can be sent

s3 = socket.socket()         # Create a socket object
host3 = '10.0.0.3' # Get local machine name
port3 = 12350                 # Reserve a port for your service.
s3.connect((host3, port3))        # Bind to the port

while True:
    command = input("Enter a command (Start, Continue, Restart): ")
    s3.send(command.encode())