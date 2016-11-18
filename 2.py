import socket
import time
import sys
import struct
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',8003))
s.listen(5)
connection,add=s.accept()
while True:
    try:
        connection.settimeout(5)
        se=connection.recv(1024)
        re=struct.unpack("5sII",se)
        filename=re[0]
        fliesize=re[2]
        i=0
        filere=open('2.bmp','wb')
	time1=time.time()
        while i< re[2]:
           temp=connection.recv(1024)
           i+=1
           filere.write(temp)
	time2=time.time()
	print time2-time1
    except:
        break
    connection.close()
