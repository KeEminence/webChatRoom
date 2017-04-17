from time import time
import socket,select,threading,sys;

# host=socket.gethostname()
host='localhost'
addr=(host,12321)

s=socket.socket()
s.connect(addr)
s.send("haha")

def lis():
	me=[s]
	while True:
		r,w,e=select.select(me,[],[])
		if s in r:
			try:
				print s.recv(1024)
			except socket.error:
				print "socket is error"
				exit()

def receivedata():
	while True:
		data=s.recv(1024)
		print data
	s.close()

def run():
	t0=threading.Thread(target=receivedata,args=())
	t0.start()
	t1=threading.Thread(target=lis,args=())
	t1.start()

run()
