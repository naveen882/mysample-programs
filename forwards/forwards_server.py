# http://www.binarytides.com/python-socket-programming-tutorial/
import socket
import sys
from thread import *
from urllib3 import *

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8889 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

conn, addr = s.accept()
 
#display client information
print 'Connected with ' + addr[0] + ':' + str(addr[1])

def forward_and_reply(host):
	print "In forward and reply"
	#Assuming client ip to be something like, this actually comes from the configuration
	client_ip = "192.168.1.1"
	port = "7777"
	#http_pool = urllib3.connection_from_url("https://yahoomail.com")
	myheaders = {'Cookie':'some cookie data'}
	#r = http_pool.get_url("http://example.org/", headers=myheaders)
	#r = http_pool.get_url("https://yahoomail.com/")
	#urllib3.get_url("https://www.yahoomail.com", fields=None)
	#r = http_pool.get_url("https://yahoomail.com",fields=None)
	#pool = HTTPConnectionPool('google.com', max)
	#r = pool.request('GET', '/search',
   #fields=None)
	conn = connection_from_url('74.125.236.210')
	r = conn.request('GET', '/')
	return r.data


def clientthread(conn):
    #Sending message to connected client
    print "hereereeeee"
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
    print "hereereeeee1"
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
        conn.send("here1")
         
        #Receiving from client
        #data = conn.recv(1024)
        #reply = 'OK...' + data
        #if not data:
        #    break
     
        #conn.sendall(reply)
        #return forward_and_reply()
        response =  forward_and_reply("12")
        print "11"
        print response
        print "22"
        #conn.send(response)
        conn.sendall(response)
        conn.close()
        break
     
    #came out of loop




while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))

s.close()


