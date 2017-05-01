# from time import time
# import socket,select,threading,sys;

# host='localhost'
# addr=(host,12321)

# s=socket.socket()
# s.connect(addr)
# s.send("a")

# def sendMessage():
# 	mes=raw_input("please input the data you want to send:")
# 	if mes:
# 		s.send(mes)

# def receiveMessage():
# 	while 1:
# 		rec=s.recv(1024)
# 		print rec

# sendMessage()
# receiveMessage()

# import sqlite3

# conn=sqlite3.connect('/root/test.db')
# cursor=conn.execute("select * from user order by username desc limit 1")
# for tmp in cursor:
# 	a=tmp[0]
# 	b=tmp[1]
# 	print a
# 	print b
# conn.close()

# import time
# ISOTIMEFORMAT='%Y-%m-%d %X'
# ti=time.strftime(ISOTIMEFORMAT,time.localtime())
# print type(ti)

