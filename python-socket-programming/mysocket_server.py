# http://www.binarytides.com/python-socket-programming-tutorial/
"""
The other kind of socket activity is called a SERVER. A server is a system that uses sockets to receive incoming connections and provide them with data. It is just the opposite of Client. So www.google.com is a server and your web browser is a client. Or more technically www.google.com is a HTTP Server and your web browser is an HTTP client.

Now its time to do some server tasks using sockets.
Programming socket servers

OK now onto server things. Servers basically do the following :

1. Open a socket
2. Bind to a address(and port).
3. Listen for incoming connections.
4. Accept connections
5. Read/Send

We have already learnt how to open a socket. So the next thing would be to bind it.
Bind a socket

Function bind can be used to bind a socket to a particular address and port. It needs a sockaddr_in structure similar to connect function.

Quick example
"""

import socket
import sys
from thread import *

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'

#Now that bind is done, its time to make the socket listen to connections. We bind a socket to a particular IP address and a certain port number. By doing this we ensure that all incoming data which is directed towards this port number is received by this application.

#This makes it obvious that you cannot have 2 sockets bound to the same port. There are exceptions to this rule but we shall look into that in some other article.
#Listen for incoming connections

#After binding a socket to a port the next thing we need to do is listen for connections. For this we need to put the socket in listening mode. Function socket_listen is used to put the socket in listening mode. Just add the following line after bind.

s.listen(10)
print 'Socket now listening'


#The parameter of the function listen is called backlog. It controls the number of incoming connections that are kept "waiting" if the program is already busy. So by specifying 10, it means that if 10 connections are already waiting to be processed, then the 11th connection request shall be rejected. This will be more clear after checking socket_accept.

#Now comes the main part of accepting new connections.
#Accept connection

#Function socket_accept is used for this.
#wait to accept a connection - blocking call
conn, addr = s.accept()
 
#display client information
print 'Connected with ' + addr[0] + ':' + str(addr[1])

#So now this program is waiting for incoming connections on port 8888. Dont close this program , keep it running.
#Now a client can connect to it on this port. We shall use the telnet client for testing this. Open a terminal and type
#
#$ telnet localhost 8888
#
#It will immediately show
#
#$ telnet localhost 8888
#Trying 127.0.0.1...
#Connected to localhost.
#Escape character is '^]'.
#Connection closed by foreign host.
#
#And the server output will show
#
#$ python server.py
#Socket created
#Socket bind complete
#Socket now listening
#Connected with 127.0.0.1:59954
#So we can see that the client connected to the server. Try the above steps till you get it working perfect.

#We accepted an incoming connection but closed it immediately. This was not very productive. There are lots of things that can be done after an incoming connection is established. Afterall the connection was established for the purpose of communication. So lets reply to the client.

#Function sendall can be used to send something to the socket of the incoming connection and the client should see it. Here is an example :

#now keep talking with the client
#Run the above code in 1 terminal. And connect to this server using telnet from another terminal and you should see this :

#$ telnet localhost 8888
#Trying 127.0.0.1...
#Connected to localhost.
#Escape character is '^]'.
#happy
#happy
#Connection closed by foreign host.

#So the client(telnet) received a reply from server.

#We can see that the connection is closed immediately after that simply because the server program ends after accepting and sending reply. A server like www.google.com is always up to accept incoming connections.

#It means that a server is supposed to be running all the time. Afterall its a server meant to serve. So we need to keep our server RUNNING non-stop. The simplest way to do this is to put the accept in a loop so that it can receive incoming connections all the time.
#data = conn.recv(1024)
#conn.sendall(data)


#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data:
            break
     
        conn.sendall(reply)
     
    #came out of loop
    conn.close()




while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))

#We havent done a lot there. Just put the socket_accept in a loop.

#Now run the server program in 1 terminal , and open 3 other terminals.
#From each of the 3 terminal do a telnet to the server port.

#Each of the telnet terminal would show :

#$ telnet localhost 5000
#Trying 127.0.0.1...
#Connected to localhost.
#Escape character is '^]'.
#happy
#OK .. happy
#Connection closed by foreign host.

#And the server terminal would show

#$ python server.py
#Socket created
#Socket bind complete
#Socket now listening
#Connected with 127.0.0.1:60225
#Connected with 127.0.0.1:60237
#Connected with 127.0.0.1:60239

#So now the server is running nonstop and the telnet terminals are also connected nonstop. Now close the server program. All telnet terminals would show "Connection closed by foreign host."

#Good so far. But still there is not effective communication between the server and the client. The server program accepts connections in a loop and just send them a reply, after that it does nothing with them. Also it is not able to handle more than 1 connection at a time. So now its time to handle the connections , and handle multiple connections together. 

#Handling Connections

#To handle every connection we need a separate handling code to run along with the main server accepting connections. One way to achieve this is using threads. The main server program accepts a connection and creates a new thread to handle communication for the connection, and then the server goes back to accept more connections.
#
#We shall now use threads to create handlers for each connection the server accepts.
s.close()


#Run the above server and open 3 terminals like before. Now the server will create a thread for each client connecting to it.

#The telnet terminals would show :

#$ telnet localhost 8888
#Trying 127.0.0.1...
#Connected to localhost.
#Escape character is '^]'.
#Welcome to the server. Type something and hit enter
#hi
#OK...hi
#asd
#OK...asd
#cv
#OK...cv

#The server terminal might look like this

#$ python server.py
#Socket created
#Socket bind complete
#Socket now listening
#Connected with 127.0.0.1:60730
#Connected with 127.0.0.1:60731
#
#The above connection handler takes some input from the client and replies back with the same.
#
#So now we have a server thats communicative. Thats useful now.
#Conclusion
#
#By now you must have learned the basics of socket programming in python. You can try out some experiments like writing a chat client or something similar.
#
#When testing the code you might face this error
#
#Bind failed. Error Code : 98 Message Address already in use
#
#When it comes up, simply change the port number and the server would run fine.
#
#If you think that the tutorial needs some addons or improvements or any of the code snippets above dont work then feel free to make a comment below so that it gets fixed.
