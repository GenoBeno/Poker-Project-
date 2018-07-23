# Import socket module
import socket               
port = 20000               

# Create a socket object
s = socket.socket()         
# Define the port on which you want to connect
 
# connect to the server on local computer
s.connect(('137.112.224.150', port))
s.send('max is wack'.encode())
#while True:
print (s.recv(1024))



# close the connection
    

