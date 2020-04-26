import socket
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
IP = config['inet']['ip']
PORT = config.getint('inet','port')
 
with  socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock: #AF_INET = ipv4 SOCK_STREAM = TCP PROTOCOL
    sock.bind((IP,PORT)) # '' = any possible
    sock.listen(1)
  
    conn , addr = sock.accept()
   
    print('Connected by ' , addr)

    with conn:
        while True :
            SIZE = 1024 # in bytes
            data = conn.recv(SIZE)
            
            if data == b'exit':
                break

            conn.sendall(data)

# conn.shutdown(socket.SHUT_RDWR)
# conn.close()
# if we use with context manager close auto 
