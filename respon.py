import socket
import os
import mimetypes
import subprocess

class Respon () :
	def __init__(self) :
		self.temp=''
        
	def direktori (self, url) :
		drt = url.split('/',1)[-1]
		msg='<title>{}</title><h1>{}</h1></br>'.format(url, url)
		
		try:
			if drt=='' :
				dir=os.listdir()
			else :
				dir = os.listdir(drt)
		except FileNotFoundError :
			hasil = "HTTP/1.1 404 Not Found\r\n" \
					"Content-Type: text/plain\r\n" \
					"Content-Length: 13\r\n" \
					"\r\n" \
					"404 Not Found"
			hasil = hasil.encode()
			return hasil
		
		for x in dir :
			msg+=str(x+'</br>')
		hasil = "HTTP/1.1 200 OK\r\n" \
				"Content-Type: text/html\r\n" \
				"Content-Length: {}\r\n" \
				"\r\n" \
				"{}".format(len(msg), msg)
		hasil = hasil.encode()
		return hasil

	def files(self, url) :
		drt=url.split('/',1)[-1]
		tipe=mimetypes.guess_type(drt)
		file=open(drt,'rb').read()
		hasil = "HTTP/1.1 200 OK\r\n" \
				"Content-Type: {}\r\n" \
				"Content-Length: {}\r\n" \
				"\r\n".format(tipe, len(file))
		hasil=hasil.encode()
		hasil=hasil+file
		return hasil
	
	def command(self, url) :
		drt=url.split('/',1)[-1]
		comm=drt.split('=')[-1]
		if comm=='delete' :
			comm='rm -rf ' + drt.split('=')[0]
		elif 'move' in comm :
			comm='mv ' + drt.split('=')[0] + ' ' + drt.split('?')[-1]
		elif 'new' in comm :
			if '.' in drt.split('=')[0] :
				comm='touch '
			else :
				comm='mkdir '
			comm=comm + drt.split('=')[0]
		comm=comm.split(' ')
		process=subprocess.call(comm)
		if process is 0 :
			msg='Success'
		else :
			msg='Error'
		hasil = "HTTP/1.1 200 OK\r\n" \
				"Content-Type: text/html\r\n" \
				"Content-Length: {}\r\n" \
				"\r\n" \
				"{}".format(len(msg), msg)
		hasil = hasil.encode()
		return hasil
			
		
		
			
		
