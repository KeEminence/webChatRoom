import socket,select,thread;  
  
# host=socket.gethostname()
host=''
port=12321  
addr=(host,port)  
       
inputs=[]  
fd_name={}  
  
def who_in_room(w):  
    name_list=[]  
    for k in w:  
        name_list.append(w[k])  
          
    return name_list  
  
def conn():  
    print 'runing'  
    ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    ss.bind(addr)  
    ss.listen(5)  
      
    return ss  
  
def new_coming(ss):  
    client,addr=ss.accept()  
    print 'welcome %s %s' % (client,addr)  
    wel='''''welcome into the talking room . 
    please decide your name.....'''
   
    try:  
        client.send(wel)  
        name=client.recv(1024)  
        inputs.append(client)  
        fd_name[client]=name  
          
        nameList="Some people in talking room, these are %s" % (who_in_room(fd_name))  
        client.send(nameList)  
          
    except Exception,e:  
        print e  
      
def server_run():  
  
    ss=conn()  
    inputs.append(ss)  
      
    while True:  
        r,w,e=select.select(inputs,[],[])  
        for temp in r:  
            if temp is ss:  
                new_coming(ss)  
            else:  
                disconnect=False  
                try:  
                    data= temp.recv(1024)  
                    data=fd_name[temp]+' : '+data  
                except socket.error:  
                    data=fd_name[temp]+' leave the room'  
                    disconnect=True  
                      
                if disconnect:  
                    inputs.remove(temp)  
                    print data  
                    for other in inputs:  
                        if other!=ss and other!=temp:  
                            try:  
                                other.send(data)  
                            except Exception,e:  
                                print e                      
                    del fd_name[temp]  
                      
                else:  
                    print data  
                      
                    for other in inputs:  
                        if other!=ss and other!=temp:  
                            try:  
                                other.send(data)  
                            except Exception,e:  
                                print e  
      
if __name__=='__main__':  
    server_run()  
