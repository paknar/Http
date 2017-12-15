import threading 
import socket
import sys
from respon import *

class Handler(threading.Thread) :
    def __init__ (self,client,conn) :
        threading.Thread.__init__(self)
        self.client = client
        self.conn = conn
        self.Respon=Respon()
        self.hasil=''

    def run(self) :
        self.incom()
    
    def cek(self, url) :
        if (url=='/') :
            return self.Respon.direktori(url)
        if '=' in url :
            return self.Respon.command(url)
        elif '.' in url :
            return self.Respon.files(url)
        
                    
    
    def incom (self) :
        while True :
            req=''
            while True :
                data=self.conn.recv(64)
                data=bytes.decode(data)
                req=req + data
                #print(req)
                if (req[-4:] == "\r\n\r\n"):
                    break
            if req is None :
                break
            msg=req.split('\r\n')
            msg_request=msg[0]
            print(msg_request)
            a, url, c = msg_request.split(' ')
            print (url)
            response=self.cek(url)
            #hasil = "HTTP/1.1 200 OK\r\n" \
		    #        "Content-Type: text/plain\r\n" \
		    #        "Content-Length: 7\r\n" \
		    #        "\r\n" \
		    #        "PROGJAR"
            #response=hasil.encode()
            self.conn.send(response)
        self.conn.close()
