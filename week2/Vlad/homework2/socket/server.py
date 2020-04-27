import socket
from configparser import ConfigParser
import os


#dirname
thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'config.ini')
config = ConfigParser()
#read
config.read(initfile)
#init sections
IP = config.get('socket','ip')
PORT = config.getint('socket','port')


with  socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock: #AF_INET = ipv4 SOCK_STREAM = TCP PROTOCOL
    
    sock.bind(('',PORT)) # '' = any possible
    sock.listen(1)
    conn , addr = sock.accept()
    
    print('Connected by ' , addr)
    with conn:
        while True :
            SIZE = 1024 # in bytes
            data = conn.recv(SIZE)
            
            if data == b'exit':
                break
            if data == b'test':
                print('work for server')
            conn.sendall(data)

