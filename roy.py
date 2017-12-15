import socket
import threading
import sys

#inisialisasi
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#proses binding
server_address = ('localhost', 12345)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#listening
sock.listen(1)

def response_redirect():
	hasil = "HTTP/1.1 301 Moved Permanently\r\n" \
		"Location: {}\r\n" \
		"\r\n"  . format('http://www.its.ac.id')
	return hasil

def response_teks():
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: text/plain\r\n" \
		"Content-Length: 7\r\n" \
		"\r\n" \
		"PROGJAR"
	return hasil

# fungsi melayani client
def layani_client(koneksi_client, alamat_client):
    try:
        print >> sys.stderr, 'ada koneksi dari ', alamat_client
        request_message = ''
        while True:
            data = koneksi_client.recv(64)
            data = bytes.decode(data)
            request_message = request_message + data
            if (request_message[-4:] == "\r\n\r\n"):
                break

        baris = request_message.split("\r\n")
        baris_request = baris[0]
        print baris_request

        a, url, c = baris_request.split(" ")

        if(url=='/teks') :
            respon=response_teks()
        else :
            respon = response_redirect()

        koneksi_client.send(respon)
    finally:
        # Clean up the connection
        koneksi_client.close()


while True:
    # Wait for a connection
    print >> sys.stderr, 'waiting for a connection'
    koneksi_client, alamat_client = sock.accept()
    s = threading.Thread(target=layani_client, args=(koneksi_client, alamat_client))
    s.start()

