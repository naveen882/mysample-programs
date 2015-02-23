#http://www.binarytides.com/python-socket-programming-tutorial/
#Creating a socket

#This first thing to do is create a socket. The socket.socket function does this.
#Error handling

#If any of the socket functions fail then python throws an exception called socket.error which must be caught.
#Quick Example

import socket
import sys

try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

print "Socket Created"

#Connect to a Server

#We connect to a remote server on a certain port number. So we need 2 things , IP address and port number to connect to. So you need to know the IP address of the remote server you are connecting to. Here we used the ip address of google.com as a sample. 


host = 'www.google.com'
#host = 'www.yahoo.com'
port = 80
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip


#Now that we have the ip address of the remote host/system, we can connect to ip on a certain 'port' using the connect function.

#Quick example
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip

#Sending Data

#Function sendall will simply send data.
#Lets send some data to google.com
#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"
 
try :
    #Set the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()
 
print 'Message send successfully'

#In the above example , we first connect to an ip address and then send the string message "GET / HTTP/1.1\r\n\r\n" to it. The message is actually an "http command" to fetch the mainpage of a website.

#Now that we have send some data , its time to receive a reply from the server. So lets do it.

#Receiving Data
#Function recv is used to receive data on a socket. In the following example we shall send the same message as the last example and receive a reply from the server.

reply = s.recv(4096121)
 
print reply
#Google.com replied with the content of the page we requested. Quite simple!
#Now that we have received our reply, its time to close the socket.
#Close socket

#Function close is used to close the socket.
	
s.close()

#Lets Revise

#So in the above example we learned how to :
#1. Create a socket
#2. Connect to remote server
#3. Send some data
#4. Receive a reply

#Its useful to know that your web browser also does the same thing when you open www.google.com
#This kind of socket activity represents a CLIENT. A client is a system that connects to a remote system to fetch data.
