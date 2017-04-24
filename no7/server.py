#!/usr/bin/env python

'''This program is for the server that sends and receives message from the clients'''

import socket,select,thread;
import sqlite3
import uuid
import time

# Enable the right time format 
ISOTIMEFORMAT='%Y-%m-%d %X'
ti=''

# Receive from every host's message 
host=''
port=12321  
addr=(host,port)  

# Global var     
inputs=[]  
fd_name={}  
namelist=[]

# Connect to the sqlite table key to store the in and left keyword
conn=sqlite3.connect('/root/test.db')
on=uuid.uuid1()
out=uuid.uuid1()

ons=str(on)
outs=str(out)

conn.execute("delete from key")
conn.commit()
conn.execute("insert into key (onkey,outkey) values (?,?)",(ons,outs))
conn.commit()
conn.close()

# Write the message to a file
f=open('record.txt','w')

# Return the users who are in the chat room 
def who_in_room(w):  
    name_list=[]
    for k in w:
        name_list.append(w[k])
    return name_list

# Init the pipe 
def conn():  
    print 'runing'  
    ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    ss.bind(addr)  
    ss.listen(5)       
    return ss  

# Write the message into the file and return the name of new comer and its tcp pipe  
def new_coming(ss):  
    global ti,namelist,fd_name
    ti=time.strftime(ISOTIMEFORMAT,time.localtime())
    client,addr=ss.accept() 
    # print 'welcome %s %s' % (client,addr)   
    try:   
        name=client.recv(1024)  
        inputs.append(client)  
        fd_name[client]=name  
        fdata=name+' come '+ti
        f.write(fdata)
        return (client,name)         
    except Exception,e:  
        print e  
      
def server_run():  
    global ti,namelist,fd_name
    ss=conn()  
    inputs.append(ss)       
    while True:  
        try:
            read,write,exce=select.select(inputs,[],[])  
            for temp in read:  
                if temp is ss:  
                    newComer,newComername=new_coming(ss)
                    for other in inputs:
                        # if other!=newComer and other!=ss:

                        # Tell other users that are online(inclued itself) that somebody is come to the room
                        if other!=ss:
                            try:
                                namelist=who_in_room(fd_name)
                                data=newComername+' come in the chat room; '+str(namelist)+'; '+ti+'; '+ons
                                # Send aone string message to promise the security
                                other.send(data)
                            except Exception,e:
                                print e               
                else:  
                    disconnect=False  
                    try:  
                        data= temp.recv(1024)  
                        if data:
                        	# chat message
                            data=fd_name[temp]+' : '+data 
                            f.write(data)
                        else:
                        	# some left room because no message was sent
                            leaveName=fd_name[temp]
                            disconnect=True 
                    except socket.error:  
                        leaveName=fd_name[temp]
                        disconnect=True  
                          
                    if disconnect:  
                        inputs.remove(temp)  
                        del fd_name[temp] 
                        namelist=who_in_room(fd_name)
                        ti=time.strftime(ISOTIMEFORMAT,time.localtime())
                        data=leaveName+' leave the chat room; '+str(namelist)+'; '+ti+'; '+ons
                        fdata=leaveName+' left '+ti
                        f.write(fdata)
                        for other in inputs:  
                            if other!=ss and other!=temp:  
                                try:  
                                    other.send(data) 
                                except Exception,e:  
                                    print e                                                
                    else:  
                    	# Send the chat message
                        for other in inputs:  
                            if other!=ss and other!=temp:  
                                try:  
                                    other.send(data)  
                                except Exception,e:  
                                    print e  
        except Exception,e:
            f.close()
     
if __name__=='__main__':  
    server_run()  

