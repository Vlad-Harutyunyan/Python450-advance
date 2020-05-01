import socket
from configparser import ConfigParser
import os

import datetime

#dirname
thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'config.ini')
config = ConfigParser()
#read
config.read(initfile)
#init sections
IP = config.get('socket','ip')
PORT = config.getint('socket','port')


with  socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock: 
    sock.bind(('',PORT))
    sock.listen(4)
    conn , addr = sock.accept()
    
    print('Connected by ' , addr)
    with conn:
        while True :
            d = datetime.datetime.now()
            commands = {'time':f'{d.hour}:{d.minute}','month':str(d.month),'year':str(d.year),'day':str(d.day)}
            SIZE = 1024 # in bytes
            data = conn.recv(SIZE).decode()
            print('used command ` : ',data)   
            r = None
            if data == 'exit':
                break
            elif data in commands :
                r = commands[data]
            elif data == 'help':
                r = 'commands ` \n 1) day - return current day \n 2) month - return current month \n 3) time - return  current time format hour:minute  \n 4) year - return current year \n 5) exit - close program'
            else :
                r = f'Unrecognized command \'{data}\' :('
            conn.sendall(r.encode())


            
            

