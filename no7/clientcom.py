import socket,select,threading,sys;

host='localhost'
addr=(host,12321)
MAX=2048

def con(username):
	clientsock=socket.socket()
	clientsock.connect(addr)
	clientsock.send(username)

def sendMessage():
	pass


def receiveMessage():
	pass
