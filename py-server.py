#!/usr/bin/python3

import socket

print("---> create  a socket object")
s = socket.socket()  # Create a socket object

print("----> getting local machine name")
host = socket.gethostname()
print("----> machine name : ", host)
print("----> assigning the port")
port = 12345
print("----> binding the port : ", port)
s.bind((host, port))

print("----> waiting for the client connection for 5 seconds")
s.listen(5)
while True:
    print("---> establish the connection with the client")
    c, addr = s.accept()
    print('Got connection from', addr)
    message = 'I LOVE CODING IN OOP BASED LANGUAGES AND SCRIPTING LANGUAGES'
    print("---> for py3, you encode the message to ascii before sending else TypeError will be thrown")
    c.send(message.encode('ascii'))
    print("---> closing tye connection")
    c.close()
