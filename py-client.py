#!/usr/bin/python3

import socket

print("----> creating the socket object")
s = socket.socket()
host = socket.gethostname()
print("---> machine hostname : ", host)
port = 12345
print("---> connection port for the server : ", port)

print("----> connecting to the server from the client")
s.connect((host, port))
print("---> connection done")

print("----> receiving data from the server")
response = s.recv(1024)
# we decode back the message when we receive the response
print("MESSAGE RECEIVED : ", response.decode('ascii'))

print("----> closing the connection after message is received from the server")
s.close()
print("----> socket connection closed done")
